# Quantum Mechanics

## Foundations

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| de Broglie | λ = h/p | p momentum | Non-relativistic or relativistic |
| Photon energy | E = hν = ℏω | ν frequency, ω angular freq | Always |
| Photon momentum | p = h/λ = ℏk | k wavevector | Always |
| Heisenberg uncertainty | ΔxΔp ≥ ℏ/2 | | Conjugate observables |
| Energy-time uncertainty | ΔEΔt ≥ ℏ/2 | | ΔE energy spread, Δt lifetime |
| Compton scattering | λ' − λ = (h/(m_ec))(1 − cosθ) | θ scattering angle | Photon-electron |
| Photoelectric | K_max = hν − φ | φ work function | hν > φ |
| Bohr energies | E_n = −13.6 eV/n² | n = 1,2,3,... | Hydrogen-like, Z=1 |
| Bohr radius | a₀ = ℏ²/(m_e e² k) = 0.529 Å | k = 1/(4πε₀) | Hydrogen |
| Rydberg formula | 1/λ = R_∞(1/n₁² − 1/n₂²) | n₂ > n₁ | Hydrogen |

## Schrödinger Equation

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Time-dependent | iℏ ∂ψ/∂t = Ĥψ | Ĥ Hamiltonian operator | Non-relativistic |
| Time-independent | Ĥψ = Eψ | | Stationary states |
| Free particle Ĥ | Ĥ = −ℏ²/(2m) ∇² + V(r) | | Non-relativistic |
| Probability density | ρ = |ψ|² | | Born rule |
| Normalization | ∫|ψ|² d³r = 1 | | Always |
| Probability current | j = (ℏ/(2mi))(ψ*∇ψ − ψ∇ψ*) | | General |
| Expectation value | ⟨A⟩ = ∫ψ*Âψ d³r | Â operator | Normalized ψ |
| Ehrenfest theorem | d⟨p⟩/dt = −⟨∇V⟩ | | General |

## Operators & Commutators

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Position operator | x̂ = x (position basis) | | Position representation |
| Momentum operator | p̂ = −iℏ∂/∂x | | Position representation |
| Canonical commutator | [x̂,p̂] = iℏ | | Always |
| Generalized uncertainty | ΔAΔB ≥ ½|⟨[Â,B̂]⟩| | | General |
| Compatible observables | [Â,B̂] = 0 ↔ simultaneous eigenstates | | General |
| Time evolution | |ψ(t)⟩ = e^(−iĤt/ℏ)|ψ(0)⟩ | | Time-independent Ĥ |

## 1D Problems

| System | Energy levels | Wavefunctions | Validity |
|--------|---------------|---------------|----------|
| Infinite square well (width L) | E_n = n²π²ℏ²/(2mL²) | ψ_n = √(2/L) sin(nπx/L) | n = 1,2,3,... |
| Harmonic oscillator | E_n = (n + ½)ℏω | ψ_n = (mω/(πℏ))^(1/4) (1/√(2ⁿn!)) H_n(ξ)e^(−ξ²/2), ξ = √(mω/ℏ)x | n = 0,1,2,... |
| HO ladder operators | â = √(mω/(2ℏ))(x̂ + ip̂/(mω)) | â|n⟩ = √n|n−1⟩, â†|n⟩ = √(n+1)|n+1⟩ | |
| Finite square well | Transcendental: κ = k tan(kL/2) or −k cot(kL/2) | Exponential tails outside | Bound states |
| Delta potential | E = −mα²/(2ℏ²) | ψ = (mα/ℏ²)^(1/2) e^(−mα|x|/ℏ²) | V = −αδ(x), one bound state |
| Tunneling (rectangular) | T ≈ e^(−2κa), κ = √(2m(V₀−E))/ℏ | a barrier width | E < V₀, κa ≫ 1 |

## Angular Momentum

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| L² eigenvalues | L²|l,m⟩ = ℏ²l(l+1)|l,m⟩ | l = 0,1,2,... | Orbital AM |
| Lz eigenvalues | Lz|l,m⟩ = ℏm|l,m⟩ | m = −l,...,+l | Orbital AM |
| Commutators | [Lx,Ly] = iℏLz (cyclic) | | General AM |
| Ladder operators | L±|l,m⟩ = ℏ√(l(l+1)−m(m±1))|l,m±1⟩ | L± = Lx ± iLy | General AM |
| Spin-½ | S² = (3/4)ℏ², Sz = ±ℏ/2 | | Spin-½ particles |
| Pauli matrices | σx = [[0,1],[1,0]], σy = [[0,−i],[i,0]], σz = [[1,0],[0,−1]] | S = ℏσ/2 | Spin-½ |
| Addition of AM | |j₁−j₂| ≤ J ≤ j₁+j₂ | J total, M = m₁+m₂ | Two AM |
| Clebsch-Gordan | |J,M⟩ = Σ ⟨j₁m₁;j₂m₂|JM⟩|j₁m₁⟩|j₂m₂⟩ | | General coupling |

## Hydrogen Atom

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Energy levels | E_n = −m_e e⁴/(2ℏ²(4πε₀)²) × 1/n² = −13.6 eV/n² | n = 1,2,3,... | Non-relativistic, infinite nucleus |
| Degeneracy | g_n = 2n² (with spin) | | Without fine structure |
| Radial wavefunctions | R_nl(r) involves L_n^(2l+1)(2r/(na₀)) × e^(−r/(na₀)) | | Laguerre polynomials |
| Angular wavefunctions | Y_l^m(θ,φ) = spherical harmonics | | |
| Selection rules (E1) | Δl = ±1, Δm = 0,±1 | | Electric dipole |
| Fine structure | ΔE = −E_n α²/n² (j(j+1)−l(l+1)−3/4)/(2l(l+½)(l+1)) + ... | | Relativistic + spin-orbit |

## Perturbation Theory

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| 1st order energy | E_n^(1) = ⟨n⁰|H'|n⁰⟩ | H' perturbation | Non-degenerate |
| 1st order state | |n^(1)⟩ = Σ_{m≠n} ⟨m⁰|H'|n⁰⟩/(E_n⁰−E_m⁰) |m⁰⟩ | | Non-degenerate |
| 2nd order energy | E_n^(2) = Σ_{m≠n} |⟨m⁰|H'|n⁰⟩|²/(E_n⁰−E_m⁰) | | Non-degenerate |
| Degenerate case | Diagonalize H' in degenerate subspace | | Degenerate levels |
| Fermi golden rule | Γ = (2π/ℏ)|⟨f|H'|i⟩|² ρ(E_f) | ρ density of final states | Time-dependent, harmonic |
| Variational principle | ⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀ | | Ground state |
| WKB quantization | ∮p dx = (n + ½)2πℏ | | Slowly varying potential |

## Identical Particles

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Bosons | ψ(1,2) = ψ(2,1) | Symmetric | Integer spin |
| Fermions | ψ(1,2) = −ψ(2,1) | Antisymmetric | Half-integer spin |
| Pauli exclusion | No two fermions in same quantum state | | Fermions |
| Slater determinant | ψ = (1/√(N!)) det[φ_i(r_j)] | | N fermions |
