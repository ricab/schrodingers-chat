# Electromagnetism

## Electrostatics

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Coulomb's law | F = kq₁q₂/r² r̂ | k = 1/(4πε₀) = 8.988e9 N·m²/C² | Point charges, static |
| Electric field (point) | E = kq/r² r̂ | | Point charge |
| Electric potential (point) | V = kq/r | | Point charge, V(∞)=0 |
| E from V | E = −∇V | | General |
| Gauss's law | ∮E·dA = Q_enc/ε₀ | Q_enc enclosed charge | General |
| Electric dipole moment | p = qd | d separation vector | Two charges ±q |
| Dipole field (far) | E ∝ p/r³ | | r ≫ d |
| Dipole potential | V = kp·r̂/r² | | r ≫ d |
| Energy density | u = ½ε₀E² | | Vacuum |
| PE of point charges | U = kq₁q₂/r | | Point charges |

## Conductors & Capacitors

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Capacitance | C = Q/V | | Linear dielectric |
| Parallel plate | C = ε₀A/d | A area, d separation | Uniform field, A ≫ d² |
| Cylindrical | C = 2πε₀L/ln(b/a) | a,b inner/outer radii, L length | L ≫ b |
| Spherical | C = 4πε₀ab/(b−a) | | Concentric spheres |
| Series capacitors | 1/C = Σ(1/C_i) | | Series |
| Parallel capacitors | C = ΣC_i | | Parallel |
| Energy stored | U = ½CV² = Q²/(2C) | | General |
| With dielectric | C → κC | κ dielectric constant | Linear dielectric |

## Magnetostatics

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Lorentz force | F = q(E + v×B) | | General (non-relativistic) |
| Force on wire | F = IL×B | I current, L length vector | Straight wire, uniform B |
| Biot-Savart law | dB = (μ₀/4π) I dl×r̂/r² | | Steady current |
| B of long wire | B = μ₀I/(2πr) | r distance from wire | Infinite straight wire |
| B inside solenoid | B = μ₀nI | n = N/L turns per length | Ideal (infinite) solenoid |
| B of toroid | B = μ₀NI/(2πr) | N total turns | Inside toroid |
| Ampère's law | ∮B·dl = μ₀I_enc | | Steady currents (no displacement) |
| Magnetic dipole moment | m = NIA n̂ | N turns, A area | Current loop |
| Torque on dipole | τ = m×B | | Uniform B |
| PE of dipole | U = −m·B | | Uniform B |

## Faraday & Induction

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Magnetic flux | Φ_B = ∫B·dA | | General |
| Faraday's law | ε = −dΦ_B/dt | ε = EMF | General |
| Motional EMF | ε = ∫(v×B)·dl | | Moving conductor |
| Self-inductance | ε = −L dI/dt | L inductance | General |
| Solenoid inductance | L = μ₀n²Aℓ | A cross-section, ℓ length | Ideal solenoid |
| Mutual inductance | ε₁ = −M dI₂/dt | M = M₁₂ = M₂₁ | General |
| Energy in inductor | U = ½LI² | | General |
| Energy density (B) | u = B²/(2μ₀) | | Vacuum |

## Maxwell's Equations

| Form | Equation | Name |
|------|----------|------|
| Differential | ∇·E = ρ/ε₀ | Gauss (electric) |
| Differential | ∇·B = 0 | Gauss (magnetic) |
| Differential | ∇×E = −∂B/∂t | Faraday |
| Differential | ∇×B = μ₀J + μ₀ε₀ ∂E/∂t | Ampère-Maxwell |
| Integral | ∮E·dA = Q_enc/ε₀ | Gauss (electric) |
| Integral | ∮B·dA = 0 | Gauss (magnetic) |
| Integral | ∮E·dl = −dΦ_B/dt | Faraday |
| Integral | ∮B·dl = μ₀I_enc + μ₀ε₀ dΦ_E/dt | Ampère-Maxwell |

## Electromagnetic Waves

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Wave equation | ∇²E = μ₀ε₀ ∂²E/∂t² | | Vacuum, source-free |
| Speed of light | c = 1/√(μ₀ε₀) | | Vacuum |
| E-B relation | E = cB | | Plane wave in vacuum |
| Poynting vector | S = (1/μ₀) E×B | | General |
| Intensity (avg) | I = ½ε₀cE₀² = E₀²/(2μ₀c) | E₀ amplitude | Plane wave |
| Radiation pressure | P = I/c (absorbed), 2I/c (reflected) | | Normal incidence |
| EM wave impedance | Z₀ = √(μ₀/ε₀) ≈ 377 Ω | | Vacuum |
| In medium | v = c/n, n = √(κ_eκ_m) | n index of refraction | Linear, non-dispersive |

## Circuits

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Ohm's law | V = IR | R resistance | Ohmic materials |
| Resistivity | R = ρL/A | ρ resistivity, L length, A area | Uniform cross-section |
| Power (resistor) | P = IV = I²R = V²/R | | DC or instantaneous |
| Series resistors | R = ΣR_i | | Series |
| Parallel resistors | 1/R = Σ(1/R_i) | | Parallel |
| Kirchhoff (junction) | ΣI_in = ΣI_out | | Charge conservation |
| Kirchhoff (loop) | ΣV = 0 | | Energy conservation |
| RC time constant | τ = RC | | RC circuit |
| RC charging | Q(t) = Cε(1 − e^(−t/τ)) | ε EMF | Charging from ε |
| RL time constant | τ = L/R | | RL circuit |
| RLC resonance | ω₀ = 1/√(LC) | | Series or parallel RLC |
| RLC quality factor | Q = ω₀L/R | | Series RLC |
| AC impedance (C) | Z_C = 1/(jωC) | j = √(−1) | Sinusoidal steady state |
| AC impedance (L) | Z_L = jωL | | Sinusoidal steady state |
| RMS values | V_rms = V₀/√2, I_rms = I₀/√2 | | Sinusoidal |
| Transformer | V₂/V₁ = N₂/N₁ | | Ideal transformer |

## Boundary Conditions

| Condition | Equation | At interface |
|-----------|----------|-------------|
| E tangential | E₁ₜ = E₂ₜ | No surface currents |
| E normal | ε₁E₁ₙ − ε₂E₂ₙ = σ_f | σ_f free surface charge |
| B normal | B₁ₙ = B₂ₙ | Always |
| B tangential | (B₁ₜ − B₂ₜ)/μ₀ = K_f×n̂ | K_f free surface current |
