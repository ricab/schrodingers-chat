"""Shared physical constants (CODATA 2018, exact where noted).

Single source of truth for both unit_convert.py and physics_calc.py.
"""

import math

# Universal
c = 2.99792458e8              # m/s (exact)
h = 6.62607015e-34            # J·s (exact)
hbar = h / (2 * math.pi)
G = 6.67430e-11               # m³/(kg·s²)
k_B = 1.380649e-23            # J/K (exact)
sigma_sb = 5.670374419e-8     # W/(m²·K⁴)

# Electromagnetic
e = 1.602176634e-19           # C (exact)
epsilon_0 = 8.8541878128e-12  # F/m
mu_0 = 1.25663706212e-6       # N/A²
alpha = 7.2973525693e-3       # fine-structure constant
k_e = 8.9875517923e9          # N·m²/C² (Coulomb constant)

# Atomic
m_e = 9.1093837015e-31        # kg
m_p = 1.67262192369e-27       # kg
m_n = 1.67492749804e-27       # kg
amu = 1.66053906660e-27        # kg
a_0 = 5.29177210903e-11       # m (Bohr radius)
R_inf = 1.0973731568160e7     # 1/m (Rydberg)
E_h = 4.3597447222071e-18     # J (Hartree)
mu_B = 9.2740100783e-24       # J/T (Bohr magneton)

# Thermodynamic
N_A = 6.02214076e23           # 1/mol
R = 8.314462618                # J/(mol·K)
F = 96485.33212                # C/mol (Faraday)
