#!/usr/bin/env python3
"""Evaluate physics expressions with built-in constants.

Usage: python3 physics_calc.py "<expression>"
Examples:
    python3 physics_calc.py "hbar * c / (1e-10)"
    python3 physics_calc.py "0.5 * m_e * (0.01 * c)**2"
    python3 physics_calc.py "k_B * 300"
    python3 physics_calc.py "e**2 / (4 * pi * epsilon_0 * a_0)"
"""

import ast
import math
import operator
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import constants as _const

# --- Physical constants (from shared constants module) ---
CONSTANTS = {
    # Universal
    "c": _const.c, "h": _const.h, "hbar": _const.hbar,
    "G": _const.G, "k_B": _const.k_B, "sigma_sb": _const.sigma_sb,
    # Electromagnetic
    "e": _const.e, "epsilon_0": _const.epsilon_0, "mu_0": _const.mu_0,
    "alpha": _const.alpha, "k_e": _const.k_e,
    # Atomic
    "m_e": _const.m_e, "m_p": _const.m_p, "m_n": _const.m_n,
    "amu": _const.amu, "a_0": _const.a_0, "R_inf": _const.R_inf,
    "E_h": _const.E_h, "mu_B": _const.mu_B,
    # Thermodynamic
    "N_A": _const.N_A, "R": _const.R, "F": _const.F,
    # Math constants
    "pi": math.pi,
    "e_math": math.e,             # use e_math to avoid collision with elementary charge
}

# --- Safe expression walker using AST ---
# This does NOT use eval(). It parses the expression into an AST and walks
# it node-by-node, only allowing arithmetic ops, known constants, and
# whitelisted math functions. No arbitrary code execution is possible.

ALLOWED_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
}

ALLOWED_FUNCS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "atan2": math.atan2,
    "exp": math.exp,
    "log": math.log,      # natural log
    "log10": math.log10,
    "log2": math.log2,
    "sqrt": math.sqrt,
    "abs": abs,
    "pow": pow,
    "factorial": math.factorial,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "asinh": math.asinh,
    "acosh": math.acosh,
    "atanh": math.atanh,
}


def walk_ast(node):
    """Recursively walk an AST node, computing the result safely."""
    if isinstance(node, ast.Expression):
        return walk_ast(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise ValueError(f"Unsupported constant type: {type(node.value)}")

    if isinstance(node, ast.Name):
        name = node.id
        if name in CONSTANTS:
            return CONSTANTS[name]
        raise ValueError(
            f"Unknown constant: '{name}'\n"
            f"Available: {', '.join(sorted(CONSTANTS.keys()))}"
        )

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in ALLOWED_OPS:
            raise ValueError(f"Unsupported operator: {op_type.__name__}")
        left = walk_ast(node.left)
        right = walk_ast(node.right)
        return ALLOWED_OPS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in ALLOWED_OPS:
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
        operand = walk_ast(node.operand)
        return ALLOWED_OPS[op_type](operand)

    if isinstance(node, ast.Call):
        if node.keywords:
            raise ValueError("Keyword arguments not supported")
        if isinstance(node.func, ast.Name) and node.func.id in ALLOWED_FUNCS:
            args = [walk_ast(arg) for arg in node.args]
            fn = ALLOWED_FUNCS[node.func.id]
            if fn is math.factorial:
                if len(args) != 1 or args[0] > 1000:
                    raise ValueError("factorial argument must be <= 1000")
            return fn(*args)
        func_name = node.func.id if isinstance(node.func, ast.Name) else "?"
        raise ValueError(
            f"Unknown function: '{func_name}'\n"
            f"Available: {', '.join(sorted(ALLOWED_FUNCS.keys()))}"
        )

    raise ValueError(f"Unsupported expression element: {type(node).__name__}")


def format_result(value):
    """Format result in both standard and scientific notation."""
    if value == 0:
        return "0"
    sci = f"{value:.6e}"
    if 1e-3 <= abs(value) < 1e6:
        std = f"{value:.6g}"
        if std != sci:
            return f"{std}  ({sci})"
    return sci


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        print(f"\nConstants: {', '.join(sorted(CONSTANTS.keys()))}")
        print(f"Functions: {', '.join(sorted(ALLOWED_FUNCS.keys()))}")
        sys.exit(1)

    expr = " ".join(sys.argv[1:])

    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as err:
        print(f"Syntax error in expression: {err}")
        sys.exit(1)

    try:
        result = walk_ast(tree)
        print(f"{expr}")
        print(f"= {format_result(result)}")
    except (ValueError, ZeroDivisionError, OverflowError) as err:
        print(f"Error: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
