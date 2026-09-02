## 2026-07-26

### Topic

Electrostatic force and electric field

### Progress

* Reviewed Coulomb’s law and the definition of the electric field.
* Implemented electric-field calculations for single and multiple point charges.
* Visualized the field distributions of representative charge configurations.
* Improved the plots to make the spatial relationship between charges clearer.

### Next Step

Complete the physical interpretation and verification of the electrostatic-field notebook before moving on to electric potential.

### summary
쿨롱의 법칙과 가우스의 법칙을 학습하였고 쿨롱의 법칙과 전기장에 관한 notebook을 작성하였다. 내일 가우스의 법칙을 다룰 예정이다.

---

## 2026-07-27

### Topic

Electric potential and electrostatic potential energy

### Progress

* Derived the relationships among electric field, potential difference, and potential energy.
* Implemented functions for point-charge potential, multiple-charge potential, and electrostatic potential energy.
* Began numerical cases for visualizing equipotential lines and verifying $\mathbf{E}=-\nabla V$

### Next Step

Complete the numerical verification and physical interpretation of the electric-potential cases.

### summary
전위와 전위차에 대한 개념을 학습하고 이에 대한 코드를 작성하였다.

---

## 2026-07-28

### Topic

Mathematical foundations for electromagnetism

### Progress

* Reviewed vector algebra and the geometric meaning of vector components.
* Studied Cartesian, cylindrical, and spherical coordinate systems.
* Examined differential length, area, and volume elements in each coordinate system.
* Established the mathematical foundation needed for vector calculus and Maxwell’s equations.

### Next Step

Apply these concepts to gradient, divergence, curl, and electromagnetic field calculations.

### summary
부족했던 수학적 개념을 보강하는 시간을 가졌다.

---

## 2026-07-29

### Topic

Conductors, electric current, dielectrics, and polarization

### Reviewed

* Electrostatic equilibrium in conductors
* Charge redistribution and equipotential conductors
* Difference between electrostatic equilibrium and steady current
* Electric current and current density
* Microscopic form of Ohm’s law
* Electric dipole moment and polarization
* Free charge and bound charge
* Electric displacement field
* Linear dielectric relations

### Work Completed

* Organized the conceptual structure of `03_conductors_currents_and_dielectrics.ipynb`
* Distinguished the zero-field condition inside an electrostatic conductor from the nonzero field required in a resistive wire
* Corrected the derivation of resistance from current density and conductivity
* Revised the sign conventions for electrical work, potential energy, and power
* Corrected the notation for dipole moment (\mathbf p), polarization (\mathbf P), and electric susceptibility (\chi_e)
* Reviewed the relations
  $$\mathbf P=\varepsilon_0\chi_e\mathbf E$$
  and
  $$\mathbf D=\varepsilon_0\mathbf E+\mathbf P =\varepsilon\mathbf E
  $$
* Revised the conceptual questions to clarify charge redistribution, signal propagation, and current density

### Difficulties

* Distinguishing electrical work from the change in electric potential energy
* Maintaining consistent vector and material-property notation
* Resolving Markdown and image-rendering problems caused by HTML sanitization in JupyterLab


### Result

Established the conceptual basis for understanding how conductors and dielectric materials respond differently to an electric field.

The notebook now connects electrostatics to material response through free-charge motion, electric current, bound charge, and dielectric polarization.

### Next Step

Complete the remaining corrections in the conceptual notebook and organize the unfinished numerical cases from the previous electric-potential notebook.

Afterward, add a small verified case comparing the electric field, capacitance, voltage, and stored energy of a parallel-plate capacitor with and without a dielectric.

### summary
전자기학 - 물질과 전자기장에 대해 공부하고 이에 대해 개념 정리 노트를 작성하였다.

---

## 2026-07-30

### Topic

Electric fields in dielectric materials

### Progress

* Studied polarization and the response of dielectric materials to an applied electric field.
* Examined the relationships among (\mathbf{E}), (\mathbf{D}), and (\mathbf{P}), including the assumptions behind the linear-dielectric approximation.
* Designed the structure and numerical cases for the dielectric-material notebook.
* Planned a comparison between the general constitutive relation and its linear approximation.

### Next Step

Implement the dielectric-response functions and verify the approximation through controlled parameter studies.

### summary
`02_electric_potential_and_electrostatic_energy`의 case 정리를 완료하였다. `03_conductors_currents_and_dielectrics`에 대한 case 정리를 진행할 예정이다.

---

## 2026-07-31

### Topic

Layered dielectric capacitor

### Progress

* Implemented and verified the layered-dielectric capacitor model.
* Analyzed how relative permittivity affects the electric field, voltage drop, and capacitance.
* Completed the main numerical experiment and physical interpretation.

### Next Step

Review the notebook and proceed to the next electromagnetism topic.

### Summary
`03_conductors_currents_and_dielectrics`의 case를 추가하고 이를 정리하였다.

---

## 2026-08-01

### Topic

Completion of dielectric-material response and introduction to magnetostatics

### Progress

* Completed Notebook 03 on the electric-field response of dielectric materials.
* Finalized the numerical verification and physical interpretation of the layered-dielectric capacitor model.
* Began studying magnetostatics and the Biot–Savart law.

### Next Step

Apply the Biot–Savart law to representative current distributions and begin the magnetostatic-field notebook.


### summary
비오 사바르 법칙에 대해 공부하였다.

---
## 2026-08-02

### Topic

Magnetostatic fields and current sources

### Reviewed

* Magnetic flux density as a vector field
* Lorentz force and the direction of magnetic force
* Biot–Savart law
* Magnetic field generated by an infinite straight current
* Magnetic flux and Gauss’s law for magnetism
* Ampère’s circuital law
* Relationship between the integral and differential forms of magnetostatic equations
* Distinction between the roles of the Biot–Savart law and Ampère’s law

### Progress

Completed the planned conceptual study of magnetostatics and organized the material in:

`notebooks/04_magnetostatic_fields_and_current_sources.ipynb`

The note was structured around the question of how steady currents generate magnetic fields and under what symmetry conditions those fields can be calculated efficiently. The notation, physical interpretation, and units of the electromagnetic field quantities were also reviewed and corrected.

### Difficulties

* Separating the general validity of Ampère’s law from the symmetry conditions required for convenient field calculation
* Keeping source-point and observation-point vectors consistent in the Biot–Savart law
* Expressing the physical interpretation accurately while preserving my own English writing style

### Result

The conceptual part of Note 04 is nearly complete. The main physical errors were corrected, and the note now provides a consistent transition from steady currents and the Biot–Savart law to Ampère’s law and the magnetostatic Maxwell equations.

### Next Step

Design minimal numerical cases that verify the analytical magnetic fields and compare the Biot–Savart and Ampère-law approaches under appropriate symmetry conditions.

### summary
비오-사바르 법칙에 이어 앙페르의 법칙과 자속밀도 벡터에 대한 학습을 진행하고 이에 대한 개념을 `notebooks/04_magnetostatic_fields_and_current_sources.ipynb`에 정리하였다. 

---

## 2026-08-03

### Topic

Implementation and verification of magnetostatic field models

### Reviewed

* Vector geometry for an infinite straight current
* Numerical verification using analytical solutions
* Inverse-distance dependence of the magnetic-field magnitude
* Physical meaning of (B\rho=\text{constant})

### Progress

Implemented the magnetic-field calculation for an arbitrarily oriented infinite straight wire in magnetostatics.py and added the first case study to:

`notebooks/04_magnetostatic_fields_and_current_sources.ipynb`

The calculated field was compared with the analytical solution, and its magnitude, direction, and distance dependence were examined.

### Difficulties

* Expressing the perpendicular displacement from an arbitrarily oriented wire

### Result

Case 1 now provides a minimal verification of the infinite-straight-wire model and establishes the structure for the remaining magnetostatic case studies.

### Next Step

Add Case 2 for a finite straight wire, Case 3 for a circular current loop, and optionally Case 4 for a distributed current using Ampère’s law.

### summary

자기장 해석에 사용할 함수를 작성하고 , 해석해 비교 및 거리 의존성 검증을 Case 1로 정리하였다.

---

## 2026-08-04

### Topic

Completion and verification of magnetostatic field case studies

### Reviewed

* Convergence of a finite straight wire toward the infinite-wire limit
* Axial magnetic field of a circular current loop
* Normalization using (z/a) and (B_z/B_0)
* Validity range of the magnetic dipole approximation
* Quantitative evaluation using relative error

### Progress

Completed the remaining magnetostatic case studies in:

`notebooks/04_magnetostatic_fields_and_current_sources.ipynb`

The finite-wire model was compared with the infinite-wire solution, and the circular-loop field was verified against its analytical axial-field expression. The exact loop field was also compared with the magnetic dipole approximation to determine the region in which the approximation becomes sufficiently accurate.

The main normalized and error-based graphs were saved in:

`figures/04_magnetostatic_fields_and_current_sources/`

### Difficulties

* Distinguishing discretization error from the physical difference between finite and infinite wires
* Determining the validity range of the dipole approximation quantitatively rather than visually

### Result

Cases 2 and 3 now verify the finite straight wire and circular current loop models through analytical comparisons, limiting behavior, normalization, and relative-error analysis. The magnetostatic notebook now contains a complete progression from an infinite straight wire to a finite wire, a current loop, and its far-field dipole approximation.

### Next Step

Review and finalize the conceptual sections of the magnetostatics notebook, then proceed to vector calculus and the remaining electromagnetic-field concepts required for the wave-optics stage.

### summary

유한 직선 도선과 원형 전류 고리의 자기장을 해석해와 비교하여 검증하고, 정규화 및 상대오차 분석을 통해 무한 도선 극한과 자기 쌍극자 근사의 유효 범위를 정리하였다.

---
## 2026-08-05

### Topic

Magnetic forces and magnetic materials

### Reviewed
* Lorentz force on moving charges
* Magnetic force on current-carrying conductors
* Force between parallel currents
* Torque and magnetic dipole moment of a current loop
* Magnetization and magnetic field intensity
* Magnetic susceptibility and permeability
* Classification of magnetic materials
* Distinction between (\mathbf{B}), (\mathbf{H}), and (\mathbf{M})

### Progress

Completed the conceptual study of magnetic forces and magnetic materials and organized the initial material in:

`notebooks/05_magnetic_forces_and_magnetic_materials.ipynb`

The scope of Note 05 was reduced to the concepts directly covered in the study material and those necessary to complete the magnetostatic part of the project. The current draft was reviewed for physical and notational consistency, particularly in the descriptions of the force between parallel currents, torque on a current loop, magnetic dipole fields, and magnetic-material quantities.

### Difficulties

* Keeping the source wire, external magnetic field, and force-receiving wire consistent in the parallel-current derivation


### Result

The conceptual scope and correction priorities for Note 05 were established. The note will remain concise and will use a single case study on the force between two parallel current-carrying wires to connect the magnetic-field model from Note 04 with its mechanical effect.

### Next Step

Correct the remaining physical, terminological, and notational issues in Note 05. Then complete the parallel-current case by verifying the analytical force, the attraction–repulsion direction, and the inverse-distance dependence.

### summary

자기력, 자기 토크 및 자성재료의 기본 개념을 학습하고 `notebooks/05_magnetic_forces_and_magnetic_materials.ipynb` 에 정리하였다. 

## 2026-08-06

### Result

Completed the remaining magnetostatic case studies in:

`notebooks/05_magnetic_forces_and_magnetic_materials.ipynb`

### summary
`notebooks/05_magnetic_forces_and_magnetic_materials.ipynb` 노트를 완성해 업로드 하였다. 

---
## 2026-08-07

### Topic

Maxwell’s equations and the completion of the electromagnetic foundation

### Reviewed

* Continuity equation and charge conservation
* Limitation of the original Ampère’s law for time-varying fields
* Maxwell’s displacement current correction
* Differential form of Maxwell’s equations
* Derivation of the electromagnetic wave equation

### Progress

Organized the Maxwell-equation section in `06_maxwell_equations_and_electromagnetic_induction.ipynb` and connected charge conservation to the Ampère–Maxwell law. Derived the electromagnetic wave equation from Maxwell’s equations, establishing the theoretical bridge from classical electromagnetism to electromagnetic waves and photonics.

### Next Step

Complete the plane-wave interpretation and Poynting-vector section, then conclude the electromagnetism stage and proceed to electromagnetic wave optics and dielectric interfaces.

### summary
맥스웰 방정식 까지의 개념을 공부하고 이를 정리하였다.

---

## 2026-08-08

### Topic

Introduction to wave motion

### Reviewed

* Basic description of wave motion
* Relationships among wavelength, frequency, and wave speed
* Mathematical representation of traveling waves
* Physical interpretation of wave propagation

### Progress

Finished the main electromagnetism study phase and began studying wave motion as the next step toward electromagnetic wave optics and integrated photonics.

### Result

Established the basic language for describing propagating waves and started transitioning from static and time-dependent electromagnetic fields to wave-based descriptions.

### Next Step

Continue through wave motion and proceed to harmonic waves and electromagnetic wave optics, focusing on the concepts required for dielectric interfaces and optical waveguides.

### Summary

전자기학 학습을 마무리한 뒤 파동 학습을 시작하였다. 파동의 기본적인 수학적 표현과 물리적 의미를 학습하고, 이후 전자기파 및 파동광학으로 연결하기 위한 기초를 마련하였다.

## 2026-08-09

### Topic

Electromagnetic waves, energy, momentum, and radiation

### Reviewed

* Fundamental laws of electromagnetic theory
* Electromagnetic wave propagation
* Energy and momentum carried by electromagnetic fields
* Electromagnetic radiation

### Progress

Extended the study of wave motion to electromagnetic waves and reviewed how Maxwell’s equations describe propagating electromagnetic fields. Studied the transport of energy and momentum by electromagnetic waves and the basic physical origin of electromagnetic radiation.

### Result

Connected the electromagnetic theory studied previously with the wave description of light and established the physical basis for understanding optical energy transport and radiation.

### Next Step

Continue with wave optics, focusing on harmonic waves, interference, reflection and refraction, total internal reflection, and evanescent fields as preparation for dielectric waveguides.

### Summary

전자기학의 기본 법칙을 파동 관점에서 다시 연결하고, 전자기파가 에너지와 운동량을 전달하는 과정과 전자기 복사의 기본 원리를 학습하였다. 이를 통해 기존의 전자기학 학습을 광학과 광집적회로에 필요한 파동적 기술로 연결하기 시작하였다.

---

## 2026-08-10

### Topic

Light in bulk matter and the electromagnetic spectrum

### Reviewed

- Electromagnetic energy flow and the Poynting vector
- Time-averaged irradiance
- Momentum density and radiation pressure
- Propagation of light in matter
- Electromagnetic-photon spectrum

### Key Takeaway

Reviewed how electromagnetic waves transport both energy and momentum, and connected the Poynting vector with irradiance, momentum flux, and radiation pressure. Completed the introductory treatment of light in bulk matter and the electromagnetic spectrum.

### Next Step

Study Rayleigh scattering, reflection and refraction, and Fermat's principle.

### summary
기존 진도를 복습하고 빛의 전파 단원을 마무리하였다.

---

## 2026-08-11

### Topic

Scattering, reflection, refraction, and Fermat's principle

### Reviewed

- Rayleigh scattering
- Reflection of light
- Refraction and Snell's law
- Fermat's principle and optical path

### Key Takeaway

Studied how light changes its propagation at material interfaces and connected Snell's law with Fermat's principle. Also reviewed Rayleigh scattering as a basic mechanism of light–matter interaction.

### Next Step

Study the electromagnetic treatment of reflection and refraction, followed by total internal reflection.

### summary 
레일리 산란, 간섭, 굴절, 반사, 페르마의 원리까지 학습하였다.

---

## 2026-08-12

#### Topic

Completion of Chapter 4: propagation of light in matter and optical phenomena

### Reviewed
Light propagation in dielectric media
Scattering and phase delay in matter
Reflection and interference at material boundaries
Fermat’s principle and related optical phenomena

### Progress

Completed the conceptual study of Chapter 4 and organized the physical ideas needed to connect electromagnetic-wave propagation with dielectric interfaces and wave optics.

### Result

Finished the main conceptual preparation for the wave-optics section and established the basis for organizing Notebook 07.

### Next Step

Structure and write the conceptual sections of `07_electromagnetic_waves_and_dielectric_interfaces.ipynb`, then proceed to the corresponding numerical cases.

### summary
chapter 4 개념학습을 완료하고 07 노트를 작성할 준비를 하였다.

---

## 2026-08-13

### Topic

Conceptual organization of electromagnetic wave optics for Notebook 07

### Reviewed

* Harmonic waves and complex representation
* Wave propagation in dielectric media
* Phase, intensity, and time-averaged quantities
* Reflection, refraction, and interference concepts
* Overall structure of the wave-optics section

### Progress

Drafted and reorganized the conceptual section of `07_electromagnetic_waves_and_dielectric_interfaces.ipynb`, focusing on the physical connections needed to transition from electromagnetic waves to dielectric interfaces and integrated photonics.

### Result

Established the main conceptual framework of Notebook 07 and clarified the notation and structure to be used before implementing the numerical cases.

### Next Step

Finalize the conceptual section and begin the minimal numerical implementation for dielectric-interface and interference cases, with analytical verification.

### summary 
`07_electromagnetic_waves_and_dielectric_interfaces.ipynb`의 개념 부분 작성을 완료하였다.

---

## 2026-08-14

### Topic

Numerical verification of Fresnel reflection and evanescent-wave behavior

### Progress

* Completed and refined the case studies in `07_electromagnetic_waves_and_dielectric_interfaces.ipynb`
* Numerically identified the Brewster angle and compared it with the analytical prediction
* Verified TE/TM power conservation using (R+T=1)
* Investigated evanescent-wave penetration depth near the critical angle and near (90^\circ)
* Examined the wavelength dependence of the penetration depth
* Selected the main figures to retain as representative results

### Result

Case 1 now verifies Fresnel reflection behavior, including the Brewster and critical angles, while Case 2 connects total internal reflection to evanescent-field confinement through the decay constant and penetration depth.

### Next Step

Finalize the physical interpretation and figure organization of Notebook 07, then move on to the next optics topic.


### summary
`07_electromagnetic_waves_and_dielectric_interfaces.ipynb`를 완성하였다.

---

## 2026-08-15

### Topic

Wave superposition

### Reviewed

* Superposition principle for waves
* Superposition of harmonic waves
* Relative phase and phase difference
* Resultant amplitude and intensity
* Physical basis of interference

### Progress

Studied the superposition of waves and examined how the relative phase and amplitudes of individual waves determine the resulting wave.

### Result

Established the conceptual basis for describing interference through the superposition of harmonic waves and prepared for the next wave-optics topics.

### Next Step

Continue with polarization and interference, then organize the concepts and numerical cases for Notebook 08.

### summary
파동의 중첩 단원을 학습하였다.

---

## 2026-08-16

### Topic

Light review of optics

### Reviewed

* Previously studied concepts in wave optics
* Key ideas related to wave propagation and superposition

### Progress

Briefly reviewed the recent optics material to maintain continuity without introducing a new topic.

### Result

Reinforced the main concepts from the previous study sessions and kept the learning flow active.

### Next Step

Resume the wave-optics sequence with polarization and interference, then continue developing Notebook 08.

---

## 2026-08-17

### Topic

Wave superposition and polarization

### Reviewed

* Superposition of harmonic waves
* Relative phase and resultant wave behavior
* Basic concepts of polarization
* Linear polarization and orthogonal field components

### Progress

Reviewed wave superposition and began studying polarization, completing approximately half of the planned polarization material.

### Result

Reinforced the connection between amplitude and relative phase in superposed waves and began extending the description of electromagnetic waves to polarization states.

### Next Step

Complete the remaining polarization material and proceed toward interference, preparing the conceptual foundation for Notebook 08.

---

## 2026-08-18

### Topic

Review and problem solving on wave superposition

### Reviewed

* Recent lecture material on wave optics
* Superposition principle for waves
* Relative phase and resultant amplitude
* Problem-solving methods for superposed waves

### Progress

Reviewed the recent lecture material and solved problems on wave superposition to reinforce the underlying concepts and equations.

### Result

Improved familiarity with applying the superposition principle to actual problems rather than only understanding it conceptually.

### Next Step

Continue with the remaining polarization material and connect polarization and interference to the structure of Notebook 08.

---

## 2026-08-19

### Topic

Matrix representation of waves

### Reviewed

* Mathematical representation of wave states using vectors and matrices
* Relation between field components and matrix notation
* Basic linear-algebraic description relevant to polarization

### Progress

Studied how wave properties can be represented in vector and matrix form, extending the previous work on superposition and polarization toward a more systematic mathematical description.

### Result

Established the basic mathematical framework needed to describe polarization states and optical transformations using linear algebra.

### Next Step

Continue with polarization and connect the matrix representation to the optical models used in Notebook 08.

---

## 2026-08-20

### Topic

Dormitory move-in and study break

### Progress

Moved into the dormitory and did not carry out additional project study.

### Result

No new technical progress was made today.

### Next Step

Resume the wave-optics sequence with polarization and its matrix representation.

---

## 2026-08-21 — 2026-08-23

### Topic

Semester preparation and project maintenance

### Progress

Focused primarily on preparations for the upcoming semester rather than new photonics material.

During this period, the mathematical-foundation notebook was also reorganized as part of preparing the repository for continued use during the semester.

### Result

Technical progress was intentionally limited while the transition to the new semester was handled.

The project remained organized so that the wave-optics work could continue without restarting or restructuring the existing study sequence.

### Next Step

Return to polarization and interference, then begin assembling the corresponding material into Notebook 08.

---

## 2026-08-24

### Topic

Completion of polarization and introduction to interference

### Reviewed

* Linear, circular, and elliptical polarization
* Orthogonal electric-field components
* Relative phase in polarization states
* Basic interference of coherent waves

### Progress

Completed the planned study of polarization and began the interference section, covering approximately half of the conceptual material.

The study connected the same amplitude-and-phase relationships used in polarization to interference between separate coherent waves.

### Result

Completed the main polarization foundation required for Notebook 08 and began connecting wave superposition directly to phase-dependent intensity.

### Next Step

Finish the interference concepts and begin organizing Notebook 08 around superposition, polarization, and interference.

---

## 2026-08-25

### Topic

Initial construction of Notebook 08

### Progress

Started writing:

`notebooks/08_wave_superposition_polarization_and_interference.ipynb`

The notebook was structured to combine the recently studied topics of wave superposition, polarization, and interference into a single progression from harmonic-field representation to phase-dependent optical behavior.

### Result

Established the initial draft and scope of Notebook 08.

The notebook will serve as the final wave-optics foundation before moving toward guided-wave and integrated-photonic models.

### Next Step

Complete and revise the conceptual sections before designing the numerical cases.

---

## 2026-08-26

### Topic

Conceptual development of Notebook 08

### Progress

Developed and reorganized the conceptual sections of:

`notebooks/08_wave_superposition_polarization_and_interference.ipynb`

The material was arranged around the relationships among harmonic fields, superposition, relative phase, polarization, and interference.

Particular attention was given to making the mathematical representation consistent with the later numerical implementation rather than treating the notebook as a general summary of optics.

### Result

Completed the main conceptual framework of Notebook 08 and established a clear transition from wave theory to the numerical study of interference and polarization.

### Next Step

Design minimal numerical cases, reuse the existing optical-field functions where appropriate, and verify the results against analytical relations.

---

## 2026-08-27

### Topic

Numerical design for interference and polarization

### Reviewed

* Complex representation of optical fields
* Intensity from complex field amplitudes
* Two-wave interference
* Interference visibility
* Jones-vector representation of polarization
* Projection of polarization states

### Progress

Extended `08_wave_superposition_polarization_and_interference.ipynb` from its conceptual draft toward numerical case studies.

The first case was structured around two-wave interference and visibility. The model uses two coherent fields with controlled amplitudes and relative phase, with analytical reference values for constructive, destructive, and quadrature-phase interference.

A second case was developed for polarization from orthogonal field components, using the vector representation introduced during the recent polarization study.

The reusable optical utilities in `src/optics.py` were also reviewed and updated so that the notebook can rely on common field, intensity, superposition, Jones-vector, and polarization-projection operations rather than repeating those calculations inside individual cells.

The mathematical-foundation notebook was additionally prepared for continued expansion during the semester, with sections reserved for Multivariable Calculus and Engineering Mathematics II.

### Verification Direction

For the interference case, numerical results will be compared directly with the analytical relation for phase-dependent intensity and with the analytical visibility obtained from the two field amplitudes.

Representative limiting cases will include equal-amplitude constructive and destructive interference and decreasing visibility under increasing amplitude imbalance.

### Result

Notebook 08 has moved from conceptual note-taking into the implementation-and-verification stage.

The numerical cases are now organized around explicit physical questions rather than general visualization, and the notebook is positioned to connect relative phase and polarization control to later Mach–Zehnder interferometer models.

### Next Step

Implement and quantitatively verify the two numerical cases, complete their physical interpretation and limitations, and close Notebook 08 before proceeding to guided-wave photonics.

---

## 2026-08-28

### Topic

Numerical verification and case development for wave interference and polarization

### Reviewed

- Complex-field representation of harmonic waves
- Phase-dependent two-wave interference
- Interference visibility under amplitude imbalance
- Numerical comparison of complex quantities
- Magnitude and phase errors for complex fields

### Progress

Continued the numerical development of:

`notebooks/08_wave_superposition_polarization_and_interference.ipynb`

Before completing the case studies, extended `verification.py` with reusable tools for comparing complex-valued results. Separate error measures were introduced for the complex value itself, its magnitude, and its phase, including appropriate treatment of phase wrapping and undefined phase at zero magnitude.

The numerical cases in Notebook 08 were then developed further around two-wave interference and polarization. The interference case was organized to compare the calculated intensity with analytical reference values at representative relative phases and to examine how amplitude imbalance affects interference visibility.

### Result

The verification framework is now better suited to the complex-valued quantities that will appear throughout the photonics part of the project.

Notebook 08 has also progressed from a conceptual draft toward an actual numerical study in which field calculations are checked quantitatively rather than interpreted from plots alone.

This establishes a reusable verification basis for later work involving polarization, waveguide modes, directional coupling, and interferometric devices.

### Next Step

Complete the remaining numerical calculations and analytical comparisons in Notebook 08, finalize the physical interpretation of the interference and polarization cases, and close the wave-optics stage before moving on to dielectric slab waveguides.

### summary
본가 가느라 케이스 스터디 다 못하고 마무리 했어용...

---

## 2026-08-29

### Topic

Numerical verification of interference and polarization in Notebook 08

### Reviewed

- Two-wave interference and phase-dependent intensity
- Polarization represented by orthogonal field components
- Jones-vector based polarization calculations
- Malus’s law
- Quantitative comparison between numerical and analytical results

### Progress

Continued implementing and testing the numerical cases in:

`notebooks/08_wave_superposition_polarization_and_interference.ipynb`

The interference and polarization sections were developed further, with emphasis on using the reusable optical-field and verification functions rather than duplicating calculations inside the notebook.

The polarization case was executed through the analyzer-angle sweep and compared with the analytical prediction from Malus’s law.

During verification, an incorrect comparison produced an unphysical maximum error of approximately 0.5. The reference quantity used in the error calculation was corrected, after which the maximum Malus-law error decreased to approximately

$$4.44\times10^{-16},$$

consistent with floating-point numerical precision.

### Result

The polarization-analysis case now reproduces Malus’s law quantitatively and provides a verified numerical connection between Jones-vector field calculations and measurable optical intensity.

The debugging process also reinforced the distinction between obtaining a plausible-looking curve and verifying that the numerical quantity being compared actually corresponds to the analytical reference.

Notebook 08 is now close to completing its main numerical-verification stage.

### Next Step

Finish the remaining physical interpretation and verification of the interference and polarization cases, review the notebook for consistency and redundant calculations, and finalize Notebook 08 before beginning the dielectric slab-waveguide stage.

### summary 
case study 내용 보강했고 내일 대구 가기 전에 결과 정리와 물리적 해석 추가할 예정입니다...

## 2026-08-30

### Topic

Finalization of Notebook 08 and repository verification structure

### Reviewed

* Physical interpretation of two-wave interference
* Relative phase and amplitude ratio in polarization
* Quarter-wave retardation and circular polarization
* Analytical verification of optical calculations
* Automated testing of reusable optics and verification functions

### Progress

Performed the final review and refinement of:

notebooks/08_wave_superposition_polarization_and_interference.ipynb

Clarified that the intensity used in the interference cases is represented by ( |\tilde{E}|^2 ) and is therefore proportional to physical optical intensity rather than expressed directly in SI units.

The physical interpretation of polarization was also refined, particularly the roles of relative phase and amplitude ratio between orthogonal field components. The quarter-wave retardation case was clarified by explicitly identifying the equal-amplitude and (\pm\pi/2) relative-phase conditions required for circular polarization.

In addition, the repository-level verification structure was expanded by introducing automated tests for the reusable optics and verification modules. The tests cover representative physical and numerical limits, including normal-incidence refraction, zero reflection between equal-index media, Fresnel power conservation, constructive and destructive interference, error calculations, phase wrapping, and invalid numerical inputs.

The README, project figure, and dependency configuration were also updated as part of the repository cleanup.

### Result

Notebook 08 now provides a verified transition from basic wave superposition to polarization and interference, completing the main wave-optics foundation required for the next stage of the project.

The addition of automated tests also establishes a basic regression-testing framework so that future changes to the reusable numerical tools can be checked against known physical limits.

### Next Step

Begin the dielectric slab-waveguide stage.

## 2026-08-31
waveguide 진도 시작하였다.

## 2026-09-01
symmetric waveguide 까지 진도 나갔다.

## 2026-09-02
공수2 과제하느라 진도 안 나갔습니다.
