---
name: physics-toolkit
description: Computational tools and reference data for physics. Use when performing unit conversions, looking up physical constants or formulas, or doing numerical physics calculations.
---

# Physics Toolkit

## Physical Constants

For exact values of fundamental constants, read [references/constants.md](references/constants.md).

For constants not listed there, WebSearch for the latest CODATA/NIST values at physics.nist.gov.

## Formula Reference

Comprehensive undergraduate formula reference, organized by topic. Read only the relevant file:

- [Classical Mechanics](references/formulas/classical-mechanics.md)
- [Electromagnetism](references/formulas/electromagnetism.md)
- [Thermodynamics & Statistical Mechanics](references/formulas/thermodynamics-stat-mech.md)
- [Quantum Mechanics](references/formulas/quantum-mechanics.md)
- [Special Relativity](references/formulas/special-relativity.md)
- [Optics](references/formulas/optics.md)
- [Waves & Oscillations](references/formulas/waves-oscillations.md)
- [Mathematical Methods](references/formulas/math-methods.md)

## Scripts

### Unit Conversion

```bash
python3 ~/.claude/skills/physics-toolkit/scripts/unit_convert.py <value> <from_unit> <to_unit>
```

Examples: `1 eV J`, `300 K eV`, `1 au m`, `1 atm Pa`

### Physics Calculator

```bash
python3 ~/.claude/skills/physics-toolkit/scripts/physics_calc.py "<expression>"
```

Built-in constants: c, hbar, h, k_B, G, e, m_e, m_p, epsilon_0, mu_0, N_A, sigma_sb, alpha, a_0, R_inf

Examples: `"hbar * c / (1e-10)"`, `"0.5 * m_e * (0.01 * c)**2"`, `"k_B * 300"`

Both scripts use only the Python standard library.
