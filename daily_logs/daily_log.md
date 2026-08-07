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
