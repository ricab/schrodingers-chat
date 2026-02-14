# Special Relativity

## Lorentz Transformations

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Lorentz factor | γ = 1/√(1 − v²/c²) = 1/√(1 − β²) | β = v/c | v < c |
| Time dilation | Δt = γΔt₀ | Δt₀ proper time | Inertial frames |
| Length contraction | L = L₀/γ | L₀ proper length | Along direction of motion |
| x-transform | x' = γ(x − vt) | | S' moves at v along x |
| t-transform | t' = γ(t − vx/c²) | | S' moves at v along x |
| Inverse transforms | x = γ(x' + vt'), t = γ(t' + vx'/c²) | | S' → S |
| Velocity addition | u' = (u − v)/(1 − uv/c²) | u velocity in S, u' in S' | Collinear |
| Transverse velocity | u_y' = u_y/(γ(1 − uv/c²)) | | v along x |

## Spacetime & Invariants

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Spacetime interval | ds² = −c²dt² + dx² + dy² + dz² | | (−,+,+,+) convention |
| Invariant interval | Δs² = −c²Δt² + Δr² | Δs² < 0 timelike, > 0 spacelike | Inertial frames |
| Proper time | dτ = dt/γ = √(−ds²)/c | | Along worldline |
| 4-position | x^μ = (ct, x, y, z) | | Contravariant |
| 4-velocity | u^μ = γ(c, v) | u^μu_μ = −c² | (−,+,+,+) signature |
| 4-momentum | p^μ = (E/c, p) | | |
| 4-force | f^μ = dp^μ/dτ | | |

## Energy & Momentum

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Relativistic momentum | p = γmv | m rest mass | v < c |
| Total energy | E = γmc² | | Massive particle |
| Rest energy | E₀ = mc² | | Always |
| Kinetic energy | K = (γ − 1)mc² | | Massive particle |
| Energy-momentum relation | E² = (pc)² + (mc²)² | | Always (massive or massless) |
| Massless particles | E = pc = hν | | Photons, m = 0 |
| Low-v expansion | K ≈ ½mv² + (3/8)mv⁴/c² + ... | | v ≪ c |

## Relativistic Dynamics

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Force | F = dp/dt = d(γmv)/dt | | General |
| 4-momentum conservation | Σp^μ_initial = Σp^μ_final | | Isolated system |
| Invariant mass | (Mc²)² = (ΣE)² − (Σpc)² | M system mass | Any frame |
| Compton scattering | λ' − λ = (h/(mc))(1 − cosθ) | | Photon-particle |
| Threshold energy | (ΣE)² − (Σpc)² ≥ (Σm_products c²)² | | Particle creation |

## Relativistic Doppler

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Longitudinal Doppler | f_obs = f_source √((1+β)/(1−β)) | β > 0 approaching | Source-observer collinear |
| Transverse Doppler | f_obs = f_source/γ | | Perpendicular motion |
| Relativistic aberration | cosθ' = (cosθ − β)/(1 − β cosθ) | θ in S, θ' in S' | General |

## Relativistic Electrodynamics

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| E-B transformation (∥) | E'_∥ = E_∥, B'_∥ = B_∥ | ∥ to relative velocity | Between inertial frames |
| E-B transformation (⊥) | E'_⊥ = γ(E + v×B)_⊥ | ⊥ to relative velocity | Between inertial frames |
| B-E transformation (⊥) | B'_⊥ = γ(B − v×E/c²)_⊥ | | Between inertial frames |
| EM invariants | E·B = invariant, E²−c²B² = invariant | | Under Lorentz transf. |
| Field tensor | F^μν (antisymmetric 4×4) | | Covariant formulation |
