#!/usr/bin/env python3
"""Convert between physical units via SI intermediate.

Usage: python3 unit_convert.py <value> <from_unit> <to_unit>
Examples:
    python3 unit_convert.py 1 eV J
    python3 unit_convert.py 300 K eV
    python3 unit_convert.py 1 au m
    python3 unit_convert.py 1 atm Pa
"""

import sys
import math
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from constants import c as _c, h as _h, hbar as _hbar, k_B as _k_B, e as _e, N_A as _N_A

# --- Unit definitions: {name: (factor_to_SI, dimension_key)} ---
# Temperature handled separately below.

UNITS = {
    # Length (SI: m)
    "m": (1.0, "length"), "km": (1e3, "length"), "cm": (1e-2, "length"),
    "mm": (1e-3, "length"), "um": (1e-6, "length"), "nm": (1e-9, "length"),
    "pm": (1e-12, "length"), "fm": (1e-15, "length"),
    "A": (1e-10, "length"), "angstrom": (1e-10, "length"),
    "au": (1.495978707e11, "length"), "AU": (1.495978707e11, "length"),
    "ly": (9.4607304725808e15, "length"),
    "pc": (3.0856775814913673e16, "length"),
    "mi": (1609.344, "length"), "ft": (0.3048, "length"),
    "in": (0.0254, "length"), "yd": (0.9144, "length"),
    "a0": (5.29177210903e-11, "length"), "bohr": (5.29177210903e-11, "length"),

    # Mass (SI: kg)
    "kg": (1.0, "mass"), "g": (1e-3, "mass"), "mg": (1e-6, "mass"),
    "ug": (1e-9, "mass"), "tonne": (1e3, "mass"),
    "lb": (0.45359237, "mass"), "oz": (0.028349523125, "mass"),
    "amu": (1.66053906660e-27, "mass"), "u": (1.66053906660e-27, "mass"),
    "m_e": (9.1093837015e-31, "mass"), "m_p": (1.67262192369e-27, "mass"),

    # Time (SI: s)
    "s": (1.0, "time"), "ms": (1e-3, "time"), "us": (1e-6, "time"),
    "ns": (1e-9, "time"), "ps": (1e-12, "time"), "fs": (1e-15, "time"),
    "min": (60.0, "time"), "hr": (3600.0, "time"), "day": (86400.0, "time"),
    "yr": (3.15576e7, "time"),

    # Energy (SI: J)
    "J": (1.0, "energy"), "kJ": (1e3, "energy"), "mJ": (1e-3, "energy"),
    "eV": (_e, "energy"), "keV": (1e3 * _e, "energy"),
    "MeV": (1e6 * _e, "energy"), "GeV": (1e9 * _e, "energy"),
    "TeV": (1e12 * _e, "energy"),
    "erg": (1e-7, "energy"), "cal": (4.184, "energy"),
    "kcal": (4184.0, "energy"), "kWh": (3.6e6, "energy"),
    "Ry": (13.605693122994 * _e, "energy"),
    "Ha": (27.211386245988 * _e, "energy"), "hartree": (27.211386245988 * _e, "energy"),

    # Force (SI: N)
    "N": (1.0, "force"), "kN": (1e3, "force"), "dyn": (1e-5, "force"),
    "lbf": (4.44822, "force"),

    # Pressure (SI: Pa)
    "Pa": (1.0, "pressure"), "kPa": (1e3, "pressure"), "MPa": (1e6, "pressure"),
    "GPa": (1e9, "pressure"), "bar": (1e5, "pressure"), "mbar": (100.0, "pressure"),
    "atm": (101325.0, "pressure"), "torr": (133.322, "pressure"),
    "mmHg": (133.322, "pressure"), "psi": (6894.757, "pressure"),

    # Power (SI: W)
    "W": (1.0, "power"), "kW": (1e3, "power"), "MW": (1e6, "power"),
    "GW": (1e9, "power"), "hp": (745.7, "power"),

    # Frequency (SI: Hz)
    "Hz": (1.0, "frequency"), "kHz": (1e3, "frequency"),
    "MHz": (1e6, "frequency"), "GHz": (1e9, "frequency"),
    "THz": (1e12, "frequency"),

    # Angle (SI: rad)
    "rad": (1.0, "angle"), "deg": (math.pi / 180, "angle"),
    "arcmin": (math.pi / 10800, "angle"), "arcsec": (math.pi / 648000, "angle"),

    # Electric charge (SI: C)
    "C": (1.0, "charge"), "mC": (1e-3, "charge"), "uC": (1e-6, "charge"),
    "nC": (1e-9, "charge"),

    # Magnetic field (SI: T)
    "T": (1.0, "Bfield"), "mT": (1e-3, "Bfield"), "uT": (1e-6, "Bfield"),
    "G": (1e-4, "Bfield"), "gauss": (1e-4, "Bfield"),

    # Area (SI: m²)
    "barn": (1e-28, "area"), "m2": (1.0, "area"), "cm2": (1e-4, "area"),

    # Speed (SI: m/s)
    "m/s": (1.0, "speed"), "km/s": (1e3, "speed"), "km/h": (1/3.6, "speed"),
    "mph": (0.44704, "speed"), "kn": (0.514444, "speed"),
}

# --- Cross-dimension conversions via physical constants ---
CROSS = {
    # Energy <-> Temperature: E = k_B T
    ("energy", "temperature"): lambda val_si: val_si / _k_B,
    ("temperature", "energy"): lambda val_si: val_si * _k_B,
    # Energy <-> Frequency: E = h nu
    ("energy", "frequency"): lambda val_si: val_si / _h,
    ("frequency", "energy"): lambda val_si: val_si * _h,
    # Energy <-> Wavelength (in m): E = hc/lambda
    ("energy", "length"): lambda val_si: _h * _c / val_si,
    ("length", "energy"): lambda val_si: _h * _c / val_si,
    # Energy <-> Mass: E = mc²
    ("energy", "mass"): lambda val_si: val_si / (_c * _c),
    ("mass", "energy"): lambda val_si: val_si * _c * _c,
    # Frequency <-> Wavelength: c = f lambda (careful: inverse)
    ("frequency", "length"): lambda val_si: _c / val_si,
    ("length", "frequency"): lambda val_si: _c / val_si,
}

# --- Temperature (absolute scales only) ---
TEMP_TO_K = {
    "K": lambda t: t,
    "C": lambda t: t + 273.15,
    "F": lambda t: (t - 32) * 5 / 9 + 273.15,
    "R": lambda t: t * 5 / 9,  # Rankine
}
K_TO_TEMP = {
    "K": lambda t: t,
    "C": lambda t: t - 273.15,
    "F": lambda t: (t - 273.15) * 9 / 5 + 32,
    "R": lambda t: t * 9 / 5,
}


def convert(value, from_unit, to_unit):
    # Temperature special case
    if from_unit in TEMP_TO_K and to_unit in K_TO_TEMP:
        if from_unit in UNITS and to_unit in UNITS:
            pass  # fall through to general case
        else:
            return K_TO_TEMP[to_unit](TEMP_TO_K[from_unit](value))
    # Temperature <-> energy cross-conversion
    if from_unit in TEMP_TO_K and to_unit in UNITS:
        to_factor, to_dim = UNITS[to_unit]
        val_K = TEMP_TO_K[from_unit](value)
        if to_dim == "energy":
            return val_K * _k_B / to_factor
        else:
            raise ValueError(f"Cannot convert temperature to {to_dim}")
    if from_unit in UNITS and to_unit in TEMP_TO_K:
        fr_factor, fr_dim = UNITS[from_unit]
        if fr_dim == "energy":
            val_J = value * fr_factor
            val_K = val_J / _k_B
            return K_TO_TEMP[to_unit](val_K)
        else:
            raise ValueError(f"Cannot convert {fr_dim} to temperature")

    # Standard conversion
    if from_unit not in UNITS:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in UNITS:
        raise ValueError(f"Unknown unit: {to_unit}")

    fr_factor, fr_dim = UNITS[from_unit]
    to_factor, to_dim = UNITS[to_unit]

    val_si = value * fr_factor

    if fr_dim == to_dim:
        return val_si / to_factor

    key = (fr_dim, to_dim)
    if key in CROSS:
        val_target_si = CROSS[key](val_si)
        return val_target_si / to_factor

    raise ValueError(
        f"Cannot convert {fr_dim} ({from_unit}) to {to_dim} ({to_unit}).\n"
        f"Supported cross-conversions: energy<->temperature, energy<->frequency, "
        f"energy<->wavelength, energy<->mass, frequency<->wavelength."
    )


def format_result(value):
    """Format with appropriate precision."""
    if abs(value) == 0:
        return "0"
    if 1e-3 <= abs(value) < 1e6:
        return f"{value:.6g}"
    return f"{value:.6e}"


def main():
    if len(sys.argv) != 4:
        print(__doc__.strip())
        print(f"\nAvailable units: {', '.join(sorted(set(list(UNITS.keys()) + list(TEMP_TO_K.keys()))))}")
        sys.exit(1)

    try:
        value = float(sys.argv[1])
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid number.")
        sys.exit(1)

    from_unit = sys.argv[2]
    to_unit = sys.argv[3]

    try:
        result = convert(value, from_unit, to_unit)
        print(f"{format_result(value)} {from_unit} = {format_result(result)} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
