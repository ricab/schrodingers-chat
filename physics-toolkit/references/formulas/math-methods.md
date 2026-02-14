# Mathematical Methods for Physics

## Vector Calculus Identities

| Name | Identity |
|------|----------|
| Gradient (Cartesian) | ∇f = (∂f/∂x)x̂ + (∂f/∂y)ŷ + (∂f/∂z)ẑ |
| Divergence | ∇·A = ∂Ax/∂x + ∂Ay/∂y + ∂Az/∂z |
| Curl | (∇×A)_i = ε_ijk ∂A_k/∂x_j |
| Laplacian (scalar) | ∇²f = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z² |
| ∇×(∇f) | = 0 (always) |
| ∇·(∇×A) | = 0 (always) |
| ∇×(∇×A) | = ∇(∇·A) − ∇²A |
| ∇(fg) | = f∇g + g∇f |
| ∇·(fA) | = f(∇·A) + A·(∇f) |
| ∇×(fA) | = f(∇×A) + (∇f)×A |
| ∇·(A×B) | = B·(∇×A) − A·(∇×B) |

## Integral Theorems

| Name | Equation | Converts |
|------|----------|----------|
| Divergence (Gauss) | ∫_V(∇·A)dV = ∮_S A·dA | Volume → surface |
| Stokes | ∫_S(∇×A)·dA = ∮_C A·dl | Surface → line |
| Gradient theorem | ∫_a^b ∇f·dl = f(b) − f(a) | Line → endpoint values |
| Green's 1st | ∫_V(f∇²g + ∇f·∇g)dV = ∮_S f(∇g)·dA | |
| Green's 2nd | ∫_V(f∇²g − g∇²f)dV = ∮_S(f∇g − g∇f)·dA | |

## Coordinate Systems

### Cylindrical (s, φ, z)

| Quantity | Expression |
|----------|------------|
| Position | r = s ŝ + z ẑ |
| ∇f | (∂f/∂s)ŝ + (1/s)(∂f/∂φ)φ̂ + (∂f/∂z)ẑ |
| ∇·A | (1/s)∂(sAs)/∂s + (1/s)∂Aφ/∂φ + ∂Az/∂z |
| ∇²f | (1/s)∂/∂s(s ∂f/∂s) + (1/s²)∂²f/∂φ² + ∂²f/∂z² |
| dV | s ds dφ dz |

### Spherical (r, θ, φ)

| Quantity | Expression |
|----------|------------|
| Position | r = r r̂ |
| ∇f | (∂f/∂r)r̂ + (1/r)(∂f/∂θ)θ̂ + (1/(r sinθ))(∂f/∂φ)φ̂ |
| ∇·A | (1/r²)∂(r²Ar)/∂r + (1/(r sinθ))∂(sinθ Aθ)/∂θ + (1/(r sinθ))∂Aφ/∂φ |
| ∇²f | (1/r²)∂/∂r(r² ∂f/∂r) + (1/(r²sinθ))∂/∂θ(sinθ ∂f/∂θ) + (1/(r²sin²θ))∂²f/∂φ² |
| dV | r² sinθ dr dθ dφ |

## Common Differential Equations

| Equation | Solution | Notes |
|----------|----------|-------|
| y' + ay = 0 | y = Ce^(−at) | Exponential decay |
| y'' + ω²y = 0 | y = A cos(ωt) + B sin(ωt) | SHM |
| y'' + 2γy' + ω₀²y = 0 | See damped oscillations | γ < ω₀: underdamped |
| x²y'' + xy' + (x²−n²)y = 0 | y = AJ_n(x) + BY_n(x) | Bessel equation |
| (1−x²)y'' − 2xy' + l(l+1)y = 0 | y = AP_l(x) + BQ_l(x) | Legendre equation |
| r²R'' + 2rR' − l(l+1)R = 0 | R = Ar^l + Br^(−l−1) | Radial (Laplace, spherical) |

## Special Functions

| Function | Definition / Key property | Appears in |
|----------|--------------------------|------------|
| Legendre P_l(x) | (1−x²)P'' − 2xP' + l(l+1)P = 0, P_l(1)=1 | Axially symmetric Laplace |
| Assoc. Legendre P_l^m | (1−x²)^(m/2) d^m/dx^m P_l(x) | Spherical harmonics |
| Spherical harmonics Y_l^m | ∝ P_l^m(cosθ)e^(imφ), orthonormal on sphere | Angular part of Laplace/Schrödinger |
| Bessel J_n(x) | Oscillatory, J_n(0)=0 for n>0 | Cylindrical symmetry |
| Hermite H_n(x) | e^(x²) (−d/dx)^n e^(−x²) | QM harmonic oscillator |
| Laguerre L_n(x) | e^x (d/dx)^n (x^n e^(−x))/n! | Hydrogen radial |
| Dirac delta δ(x) | ∫f(x)δ(x−a)dx = f(a), δ(ax) = δ(x)/|a| | Point sources, QM |
| Gamma function Γ(n) | (n−1)! for integers, Γ(½) = √π | Generalizing factorials |

## Fourier Analysis

| Name | Equation | Variables |
|------|----------|-----------|
| Fourier series | f(x) = a₀/2 + Σ(a_n cos(nπx/L) + b_n sin(nπx/L)) | Period 2L |
| Coefficients | a_n = (1/L)∫f(x)cos(nπx/L)dx, b_n = (1/L)∫f(x)sin(nπx/L)dx | Integrate over period |
| Complex form | f(x) = Σc_n e^(inπx/L), c_n = (1/2L)∫f(x)e^(−inπx/L)dx | |
| Fourier transform | F(k) = ∫f(x)e^(−ikx)dx | Physics convention |
| Inverse FT | f(x) = (1/2π)∫F(k)e^(ikx)dk | |
| Parseval's theorem | ∫|f(x)|²dx = (1/2π)∫|F(k)|²dk | Energy conservation |
| Convolution theorem | FT[f*g] = F(k)G(k) | * = convolution |

## Laplace Transform

| Name | Equation |
|------|----------|
| Definition | F(s) = ∫₀^∞ f(t)e^(−st)dt |
| e^(at) | 1/(s−a) |
| t^n | n!/s^(n+1) |
| cos(ωt) | s/(s²+ω²) |
| sin(ωt) | ω/(s²+ω²) |
| Derivative | L[f'] = sF(s) − f(0) |

## Green's Functions

| Equation | Green's function | Boundary |
|----------|-----------------|----------|
| ∇²G = δ³(r−r') | G = −1/(4π|r−r'|) | Free space, 3D |
| (∂²/∂t² − c²∇²)G = δ | Retarded: G ∝ δ(t−|r|/c)/|r| | Causal, 3D |
| General method | LG(x,x') = δ(x−x'), then u(x) = ∫G(x,x')f(x')dx' | L linear operator |

## Useful Integrals

| Integral | Result | Condition |
|----------|--------|-----------|
| ∫₀^∞ x^n e^(−ax) dx | n!/a^(n+1) | a > 0, n ≥ 0 integer |
| ∫₋∞^∞ e^(−ax²) dx | √(π/a) | a > 0 (Gaussian) |
| ∫₀^∞ x² e^(−ax²) dx | √π/(4a^(3/2)) | a > 0 |
| ∫₀^∞ x^(n−1)/(e^x−1) dx | Γ(n)ζ(n) | Bose integrals |
| ∫₀^∞ x^(n−1)/(e^x+1) dx | (1−2^(1−n))Γ(n)ζ(n) | Fermi integrals |
| ∫₀^π sin^n θ dθ | √π Γ((n+1)/2)/Γ((n+2)/2) | n > −1 |
