# Waves & Oscillations

## Simple Harmonic Motion

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Equation of motion | ẍ + ω²x = 0 | ω natural frequency | Linear restoring force |
| General solution | x(t) = A cos(ωt + φ) | A amplitude, φ phase | SHM |
| Mass-spring | ω = √(k/m), T = 2π√(m/k) | k spring const | Hooke's law |
| Simple pendulum | ω = √(g/L), T = 2π√(L/g) | L length | Small angle (θ ≪ 1) |
| Physical pendulum | ω = √(mgd/I) | d dist to CM, I about pivot | Small angle |
| Torsional | ω = √(κ/I) | κ torsion const | Linear restoring torque |
| Energy | E = ½kA² = ½mω²A² | | Constant, SHM |

## Damped Oscillations

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Equation of motion | ẍ + 2γẋ + ω₀²x = 0 | γ = b/(2m) damping rate | Linear damping |
| Underdamped | x = Ae^(−γt) cos(ω₁t + φ) | ω₁ = √(ω₀² − γ²) | γ < ω₀ |
| Critically damped | x = (A + Bt)e^(−γt) | | γ = ω₀ |
| Overdamped | x = Ae^(−α₁t) + Be^(−α₂t) | α₁,₂ = γ ∓ √(γ²−ω₀²) | γ > ω₀ |
| Quality factor | Q = ω₀/(2γ) | | Measure of sharpness |
| Energy decay | E(t) = E₀ e^(−2γt) = E₀ e^(−t·ω₀/Q) | | Underdamped |

## Driven Oscillations

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Equation of motion | ẍ + 2γẋ + ω₀²x = (F₀/m)cosωt | ω driving frequency | Sinusoidal drive |
| Steady-state amplitude | A = (F₀/m)/√((ω₀²−ω²)² + 4γ²ω²) | | Steady state |
| Phase lag | tanδ = 2γω/(ω₀²−ω²) | | Steady state |
| Resonance frequency | ω_res = √(ω₀²−2γ²) ≈ ω₀ for Q ≫ 1 | | Amplitude resonance |
| Amplitude at resonance | A_max = F₀/(2mγω₀) = QF₀/(mω₀²) | | ω = ω_res |
| FWHM bandwidth | Δω ≈ 2γ = ω₀/Q | | High Q |

## Coupled Oscillators

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Normal modes | Each mode oscillates at one frequency | | Linear coupling |
| Two coupled (symmetric) | ω₁ = √(k/m) (in-phase) | | Identical masses & springs |
| Two coupled (antisymm.) | ω₂ = √((k+2κ)/m) (out-of-phase) | κ coupling spring | Identical masses |
| Beats | x = 2A cos(Δωt/2) cos(ω̄t) | Δω = ω₂−ω₁, ω̄ = (ω₁+ω₂)/2 | Weakly coupled |
| N coupled (chain) | ω_n = 2ω₀ \|sin(nπ/(2(N+1)))\| | n = 1,...,N | Identical masses, fixed ends |

## Waves

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Wave equation | ∂²y/∂t² = v² ∂²y/∂x² | v phase velocity | Linear, non-dispersive |
| Traveling wave | y = A sin(kx − ωt + φ) | k = 2π/λ, ω = 2πf | |
| Dispersion relation | ω = vk (non-dispersive) | | General: ω = ω(k) |
| Phase velocity | v_p = ω/k = fλ | | |
| Group velocity | v_g = dω/dk | | Dispersion |
| String wave speed | v = √(T/μ) | T tension, μ linear density | Flexible string |
| Sound speed (ideal gas) | v = √(γRT/M) = √(γP/ρ) | M molar mass | Ideal gas |
| Sound speed (solid) | v = √(Y/ρ) | Y Young's modulus | Longitudinal |
| Intensity | I = ½ρvω²A² | | Mechanical wave |
| Intensity (inverse square) | I = P/(4πr²) | P power | Point source, 3D |
| Intensity level | β = 10 log₁₀(I/I₀) dB | I₀ = 10⁻¹² W/m² | Reference: threshold of hearing |

## Standing Waves

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Standing wave | y = 2A sin(kx) cos(ωt) | | Superposition of counterpropagating |
| Fixed-fixed string | λ_n = 2L/n, f_n = nv/(2L) | n = 1,2,3,... | Both ends fixed |
| Open-open pipe | λ_n = 2L/n, f_n = nv/(2L) | n = 1,2,3,... | Both ends open |
| Fixed-open pipe | λ_n = 4L/n, f_n = nv/(4L) | n = 1,3,5,... (odd only) | One end closed |

## Doppler Effect (classical)

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| General Doppler | f' = f (v ± v_obs)/(v ∓ v_source) | v sound speed | + top: approaching, source/obs |
| Source approaching | f' = f v/(v − v_s) | | Observer at rest |
| Observer approaching | f' = f (v + v_o)/v | | Source at rest |
| Mach number | M = v_source/v_sound | | Shock wave at M > 1 |
| Mach cone angle | sinθ = 1/M | | Supersonic |
