# Thermodynamics & Statistical Mechanics

## Zeroth & First Law

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| First law | dU = δQ − δW | U internal energy, Q heat in, W work out | Closed system |
| Work (gas) | δW = P dV | | Quasi-static, hydrostatic |
| Heat capacity (V) | C_V = (∂U/∂T)_V | | General |
| Heat capacity (P) | C_P = (∂H/∂T)_P | H enthalpy | General |
| C_P − C_V relation | C_P − C_V = TVα²/κ_T | α expansion coeff, κ_T compressibility | General |
| Ideal gas C_P − C_V | C_P − C_V = nR | | Ideal gas |
| Equipartition | ⟨E⟩ = ½f k_BT | f active degrees of freedom | Classical, quadratic terms |

## Ideal Gas

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Ideal gas law | PV = nRT = Nk_BT | n moles, N particles | Dilute, non-interacting |
| Isothermal work | W = nRT ln(V_f/V_i) | | Ideal gas, T = const |
| Adiabatic relation | PV^γ = const, TV^(γ−1) = const | γ = C_P/C_V | Ideal gas, adiabatic, quasi-static |
| γ values | Monatomic: 5/3, diatomic: 7/5 | | Classical |
| rms speed | v_rms = √(3k_BT/m) | m molecular mass | Ideal gas |
| Mean free path | λ = 1/(nσ√2) | n number density, σ cross-section | Ideal gas |

## Second Law & Entropy

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Entropy definition | dS = δQ_rev/T | | Reversible process |
| Clausius inequality | dS ≥ δQ/T | | General (= for reversible) |
| Entropy change (ideal gas) | ΔS = nC_V ln(T_f/T_i) + nR ln(V_f/V_i) | | Ideal gas |
| Entropy of mixing | ΔS = −nR Σx_i ln(x_i) | x_i mole fractions | Ideal mixing |
| Boltzmann entropy | S = k_B ln Ω | Ω number of microstates | Microcanonical |
| Carnot efficiency | η = 1 − T_C/T_H | T_C cold, T_H hot reservoir | Reversible heat engine |
| COP (refrigerator) | COP = T_C/(T_H − T_C) | | Reversible |

## Thermodynamic Potentials

| Potential | Definition | Natural variables | Differential |
|-----------|------------|-------------------|-------------|
| Internal energy | U | S, V, N | dU = TdS − PdV + μdN |
| Enthalpy | H = U + PV | S, P, N | dH = TdS + VdP + μdN |
| Helmholtz | F = U − TS | T, V, N | dF = −SdT − PdV + μdN |
| Gibbs | G = U − TS + PV | T, P, N | dG = −SdT + VdP + μdN |
| Grand potential | Ω = F − μN | T, V, μ | dΩ = −SdT − PdV − Ndμ |

## Maxwell Relations

| From | Relation |
|------|----------|
| U(S,V) | (∂T/∂V)_S = −(∂P/∂S)_V |
| H(S,P) | (∂T/∂P)_S = (∂V/∂S)_P |
| F(T,V) | (∂S/∂V)_T = (∂P/∂T)_V |
| G(T,P) | −(∂S/∂P)_T = (∂V/∂T)_P |

## Phase Transitions

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Clausius-Clapeyron | dP/dT = L/(TΔv) | L latent heat, Δv volume change | First-order transition |
| Van der Waals | (P + a/v²)(v − b) = RT | a,b substance-dependent, v molar vol | Approximate real gas |
| Critical point (vdW) | T_c = 8a/(27Rb), P_c = a/(27b²), v_c = 3b | | Van der Waals |
| Gibbs phase rule | F = C − P + 2 | C components, P phases, F dof | Equilibrium |

## Statistical Mechanics

| Name | Equation | Variables | Validity |
|------|----------|-----------|----------|
| Boltzmann distribution | P(E) ∝ e^(−E/(k_BT)) | | Canonical ensemble |
| Partition function | Z = Σ_i e^(−E_i/(k_BT)) | sum over microstates | Canonical |
| F from Z | F = −k_BT ln Z | | Canonical |
| ⟨E⟩ from Z | ⟨E⟩ = −∂(ln Z)/∂β | β = 1/(k_BT) | Canonical |
| Entropy from Z | S = k_B(ln Z + β⟨E⟩) | | Canonical |
| Grand partition function | Z_G = Σ_N e^(βμN) Z_N | | Grand canonical |
| Fermi-Dirac | f(E) = 1/(e^((E−μ)/(k_BT)) + 1) | μ chemical potential | Fermions |
| Bose-Einstein | f(E) = 1/(e^((E−μ)/(k_BT)) − 1) | μ ≤ 0 for bosons | Bosons |
| Maxwell-Boltzmann | f(v) = 4π(m/(2πk_BT))^(3/2) v² e^(−mv²/(2k_BT)) | | Classical, 3D speed dist. |
| Density of states (3D free) | g(E) = V/(2π²)(2m/ℏ²)^(3/2) √E | | Free particles, 3D |
| Planck distribution | ⟨n(ω)⟩ = 1/(e^(ℏω/(k_BT)) − 1) | | Photons/phonons |
| Stefan-Boltzmann law | j = σT⁴ | σ = 5.67e-8 W/(m²K⁴) | Blackbody |
| Wien's law | λ_max T = 2.898e-3 m·K | | Blackbody |
| Planck radiation | u(ν) = (8πhν³/c³)/(e^(hν/(k_BT)) − 1) | | Blackbody spectral density |
| Debye T³ law | C_V ∝ T³ | | T ≪ Θ_D (solids) |
