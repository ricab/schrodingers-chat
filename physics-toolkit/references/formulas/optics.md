# Optics

## Geometric Optics

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Snell's law | n₁ sinθ₁ = n₂ sinθ₂ | n index of refraction, θ from normal | Planar interface |
| Critical angle | sinθ_c = n₂/n₁ | | n₁ > n₂ (total internal reflection) |
| Brewster's angle | tanθ_B = n₂/n₁ | | Reflected light fully s-polarized |
| Thin lens equation | 1/s + 1/s' = 1/f | s object dist, s' image dist, f focal length | Paraxial (small angles) |
| Mirror equation | 1/s + 1/s' = 2/R = 1/f | R radius of curvature | Paraxial |
| Magnification | M = −s'/s = h'/h | h, h' object/image height | Paraxial |
| Lensmaker's equation | 1/f = (n−1)(1/R₁ − 1/R₂) | R₁, R₂ surface radii | Thin lens in air |
| Angular magnification (simple) | m = 25 cm / f | | Simple magnifier, near point 25 cm |
| Numerical aperture | NA = n sinθ_max | | Fiber optics / microscopy |
| Optical path length | OPL = ∫n dl | | General |

## Wave Optics: Interference

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Constructive interference | Δ = mλ | Δ path difference, m = 0,±1,±2,... | Coherent sources |
| Destructive interference | Δ = (m + ½)λ | | Coherent sources |
| Young's double slit (maxima) | d sinθ = mλ | d slit separation | Far field |
| Young's double slit (spacing) | Δy = λL/d | L screen distance | Small angle |
| Thin film (reflected, n₂>n₁) | 2n₂t = (m + ½)λ (constructive) | t film thickness | Normal incidence, phase shift at one surface |
| Michelson fringe shift | ΔN = 2d Δn/λ | d arm length, Δn index change | |
| Coherence length | l_c = c/Δν ≈ λ²/Δλ | Δν bandwidth | Temporal coherence |

## Wave Optics: Diffraction

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Single slit (minima) | a sinθ = mλ | a slit width, m = ±1,±2,... | Fraunhofer |
| Single slit (intensity) | I = I₀ (sinα/α)² | α = πa sinθ/λ | Fraunhofer |
| Circular aperture (Airy) | sinθ₁ = 1.22 λ/D | D diameter | First minimum |
| Rayleigh criterion | θ_min = 1.22 λ/D | | Angular resolution |
| Diffraction grating (maxima) | d sinθ = mλ | d grating spacing | |
| Grating resolving power | R = λ/Δλ = mN | N total slits, m order | |
| Bragg diffraction | 2d sinθ = nλ | d plane spacing | Crystal planes |

## Polarization

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Malus's law | I = I₀ cos²θ | θ angle between polarizer axes | Linear polarizer |
| Brewster's angle | tanθ_B = n₂/n₁ | | Reflected: pure s-polarization |
| Fresnel (s, normal) | r_s = (n₁−n₂)/(n₁+n₂) | | Normal incidence |
| Fresnel (p, normal) | r_p = (n₂−n₁)/(n₁+n₂) | | Normal incidence |
| Reflectance (normal) | R = ((n₁−n₂)/(n₁+n₂))² | | Normal incidence |
| Circular polarization | E = E₀(x̂ cosωt ± ŷ sinωt) | + RCP, − LCP | Monochromatic |

## Fresnel Equations (general angle)

| Polarization | Reflection coefficient | Transmission coefficient |
|-------------|----------------------|------------------------|
| s (TE) | r_s = (n₁cosθ₁ − n₂cosθ₂)/(n₁cosθ₁ + n₂cosθ₂) | t_s = 2n₁cosθ₁/(n₁cosθ₁ + n₂cosθ₂) |
| p (TM) | r_p = (n₂cosθ₁ − n₁cosθ₂)/(n₂cosθ₁ + n₁cosθ₂) | t_p = 2n₁cosθ₁/(n₂cosθ₁ + n₁cosθ₂) |

R = |r|², T = (n₂cosθ₂)/(n₁cosθ₁) |t|²
