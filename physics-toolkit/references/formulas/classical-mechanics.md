# Classical Mechanics

## Kinematics (constant acceleration)

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Velocity | v = v₀ + at | v₀ initial vel, a accel, t time | Constant a |
| Displacement | x = x₀ + v₀t + ½at² | x₀ initial pos | Constant a |
| Velocity-displacement | v² = v₀² + 2a(x - x₀) | | Constant a |
| Projectile range | R = v₀²sin(2θ)/g | θ launch angle | Flat ground, no drag |
| Projectile max height | H = v₀²sin²θ/(2g) | | Flat ground, no drag |
| Centripetal acceleration | a_c = v²/r = ω²r | r radius, ω angular vel | Circular motion |

## Newton's Laws & Forces

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Newton's 2nd law | F = dp/dt = ma | p momentum | Inertial frame, v ≪ c |
| Newton's 3rd law | F₁₂ = −F₂₁ | | Always (contact & field) |
| Weight | W = mg | g ≈ 9.81 m/s² near Earth | Near surface |
| Kinetic friction | f_k = μ_k N | N normal force, μ_k coeff | Sliding contact |
| Static friction | f_s ≤ μ_s N | μ_s static coeff | No sliding |
| Spring (Hooke) | F = −kx | k spring const, x displacement | Linear regime |
| Drag (low Re) | F = −bv | b drag coeff | Stokes regime, Re ≪ 1 |
| Drag (high Re) | F = −½CρAv² | C drag coeff, ρ density, A area | Turbulent, Re ≫ 1 |

## Work, Energy, Power

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Work | W = ∫F·dr | | General |
| Kinetic energy | K = ½mv² | | Non-relativistic |
| Work-energy theorem | W_net = ΔK | | General |
| Gravitational PE | U = mgh | h height | Uniform g |
| Gravitational PE (general) | U = −GMm/r | r separation | Point masses / spheres |
| Elastic PE | U = ½kx² | | Hooke's law regime |
| Power | P = dW/dt = F·v | | General |
| Conservative force | F = −∇U | U potential energy | Path-independent forces |

## Momentum & Collisions

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Linear momentum | p = mv | | Non-relativistic |
| Impulse | J = ∫F dt = Δp | | General |
| Conservation of momentum | Σp_i = const | | No external forces |
| Elastic 1D collision | v₁' = ((m₁−m₂)v₁ + 2m₂v₂)/(m₁+m₂) | | 1D, elastic |
| Center of mass | R = Σm_ir_i / Σm_i | | General |
| Rocket equation | Δv = v_e ln(m₀/m_f) | v_e exhaust vel, m₀/m_f mass ratio | Tsiolkovsky, no gravity |

## Rotational Dynamics

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Angular velocity | ω = dθ/dt | θ angle | General |
| Angular acceleration | α = dω/dt | | General |
| Torque | τ = r × F = Iα | I moment of inertia | Rigid body, fixed axis |
| Angular momentum | L = r × p = Iω | | Rigid body, fixed axis |
| Rotational KE | K_rot = ½Iω² | | Rigid body |
| Parallel axis theorem | I = I_cm + Md² | d offset distance | Rigid body |
| Rolling (no slip) | v_cm = Rω | R radius | Pure rolling |

### Common Moments of Inertia

| Shape | Axis | I |
|-------|------|---|
| Thin rod (length L) | Center, ⊥ | (1/12)ML² |
| Thin rod (length L) | End, ⊥ | (1/3)ML² |
| Solid cylinder (radius R) | Central axis | (1/2)MR² |
| Hollow cylinder (R₁, R₂) | Central axis | (1/2)M(R₁² + R₂²) |
| Solid sphere (radius R) | Any diameter | (2/5)MR² |
| Hollow sphere (radius R) | Any diameter | (2/3)MR² |
| Thin disk (radius R) | Diameter | (1/4)MR² |

## Gravitation

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Newton's law of gravitation | F = GMm/r² | G = 6.674e-11 | Point masses / spheres |
| Gravitational field | g = GM/r² | | Outside mass dist. |
| Orbital velocity (circular) | v = √(GM/r) | | Circular orbit |
| Escape velocity | v_esc = √(2GM/r) | | From distance r |
| Kepler's 3rd law | T² = (4π²/GM)a³ | a semi-major axis | Two-body |
| Gravitational PE | U = −GMm/r | | Point masses / spheres |
| Vis-viva equation | v² = GM(2/r − 1/a) | | Keplerian orbit |

## Lagrangian & Hamiltonian Mechanics

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Lagrangian | L = T − V | T kinetic, V potential | Holonomic constraints |
| Euler-Lagrange equation | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | q generalized coord | Holonomic constraints |
| Canonical momentum | p = ∂L/∂q̇ | | General |
| Hamiltonian | H = Σp_iq̇_i − L | | Legendre transform of L |
| Hamilton's equations | q̇ = ∂H/∂p, ṗ = −∂H/∂q | | General |
| H = E condition | H = T + V | | When L has no explicit t and T is quadratic in q̇ |
| Noether's theorem | Symmetry → conservation law | | Continuous symmetry of L |
| Cyclic coordinate | ∂L/∂q = 0 → p_q = const | | q absent from L |

## Fluid Statics & Dynamics (basics)

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Hydrostatic pressure | P = P₀ + ρgh | ρ fluid density | Incompressible, uniform g |
| Buoyancy (Archimedes) | F_b = ρ_fluid V_disp g | V_disp displaced vol | Any fluid |
| Continuity equation | A₁v₁ = A₂v₂ | A cross-section | Incompressible, steady |
| Bernoulli's equation | P + ½ρv² + ρgh = const | | Incompressible, inviscid, steady, along streamline |
