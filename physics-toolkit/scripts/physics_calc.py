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
import sys

# --- Physical constants (CODATA 2018) ---
CONSTANTS = {
    # Universal
    "c": 2.99792458e8,            # m/s
    "h": 6.62607015e-34,          # J·s
    "hbar": 1.054571817e-34,      # J·s
    "G": 6.67430e-11,             # m³/(kg·s²)
    "k_B": 1.380649e-23,          # J/K
    "sigma_sb": 5.670374419e-8,   # W/(m²·K⁴)

    # Electromagnetic
    "e": 1.602176634e-19,         # C
    "epsilon_0": 8.8541878128e-12, # F/m
    "mu_0": 1.25663706212e-6,     # N/A²
    "alpha": 7.2973525693e-3,     # fine-structure constant
    "k_e": 8.9875517923e9,        # N·m²/C² (Coulomb constant)

    # Atomic
    "m_e": 9.1093837015e-31,      # kg
    "m_p": 1.67262192369e-27,     # kg
    "m_n": 1.67492749804e-27,     # kg
    "amu": 1.66053906660e-27,     # kg
    "a_0": 5.29177210903e-11,     # m (Bohr radius)
    "R_inf": 1.0973731568160e7,   # 1/m (Rydberg)
    "E_h": 4.3597447222071e-18,   # J (Hartree)
    "mu_B": 9.2740100783e-24,     # J/T (Bohr magneton)

    # Thermodynamic
    "N_A": 6.02214076e23,         # 1/mol
    "R": 8.314462618,             # J/(mol·K)
    "F": 96485.33212,             # C/mol (Faraday)

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
        if isinstance(node.func, ast.Name) and node.func.id in ALLOWED_FUNCS:
            args = [walk_ast(arg) for arg in node.args]
            return ALLOWED_FUNCS[node.func.id](*args)
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
