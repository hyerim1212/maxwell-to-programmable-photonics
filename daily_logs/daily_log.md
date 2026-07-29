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