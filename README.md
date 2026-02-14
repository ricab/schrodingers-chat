# schrodingers-chat

A physics agent with (tentative) problem solving skills

## Features

- **Unit converter**: Convert between 90+ physical units across 14 dimensions with physics-aware cross-conversions (energy↔wavelength, energy↔temperature, etc.)
- **Physics calculator**: Secure expression evaluator with 30+ physical constants and standard math functions
- **Formula references**: Quick-reference sheets for 8 physics domains (classical mechanics, E&M, quantum mechanics, thermodynamics, special relativity, optics, waves, and mathematical methods)

## Installation

Link agents and skills in your user settings so it's available across all your projects.

### Link the agent and skills

```bash
mkdir -p <agent-settings>/{agents,skills}
ln -s <schrodingers-chat>/physicist.md ~/.claude/agents/physicist.md
ln -s <schrodingers-chat>/physics-toolkit ~/.claude/skills/physics-toolkit
```

- Replace `<agent-settings>` with your tool's configuration location.
    * For example: `~/.claude` when using Claude Code on Linux.
- Replace `<schrodingers-chat>` with the actual location of this repository.

### Verify installation

The skill will be automatically available in Claude Code. You can verify by asking Claude to convert units or look up physics formulas.

## Usage

### Unit Conversion

```bash
python3 scripts/unit_convert.py 1 eV J
python3 scripts/unit_convert.py 300 K eV
python3 scripts/unit_convert.py 1 au m
```

Or ask Claude: "Convert 1 eV to joules" or "What is 300 K in electron volts?"

### Physics Calculator

```bash
python3 scripts/physics_calc.py "hbar * c / (1e-10)"
python3 scripts/physics_calc.py "E_h / k_B"
python3 scripts/physics_calc.py "exp(-13.6 / (k_B * 300))"
```

Or ask Claude: "Calculate ℏc/1Å" or "What is the Hartree energy in Kelvin?"

### Formula Lookup

Ask Claude: "Show me the Maxwell equations" or "What's the Schrödinger equation for the hydrogen atom?"

## Dependencies

None. Both scripts use only Python standard library.

## Physics Constants (CODATA 2018)

Available in both scripts and in `references/constants.md`:
- Universal: c, h, ℏ, G, k_B, σ
- Electromagnetic: e, ε₀, μ₀, α, k_e, μ_B
- Atomic: m_e, m_p, m_n, a_0, R_∞, E_h
- Thermodynamic: N_A, R, F
