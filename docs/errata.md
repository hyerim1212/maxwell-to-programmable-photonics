# Errata — Corrections to Calculations and Notation, and Scope of Applicability

Date: 2026-09-07  
Review baseline: commit [`522ebeacd7e2c5c49e30b7b6a450862355cdb350`](https://github.com/hyerim1212/maxwell-to-programmable-photonics/tree/522ebeacd7e2c5c49e30b7b6a450862355cdb350)

## How to Read This Document

This document records errors identified during review and the scope of applicability of the results, while preserving the original notebooks as a record of the learning process. Documenting a proposed correction does not mean that the original code, figures, or text have been updated, or that the corrected calculations have been rerun.

Locations are identified by notebook section or Case titles and search terms, rather than line numbers in the notebook JSON. The code snippets below illustrate the proposed corrections and have not yet been applied to the originals.

The following status labels are used.

- **Error confirmed**: The issue has been confirmed from existing code or output, or by direct reproduction.
- **Correction proposed**: A correction has been proposed, but the complete corrected experiment has not been rerun.
- **Reverification complete**: The corrected experiment has been run, and its numerical results, figures, and interpretation have been checked together. No entries currently have this status.

Passing the existing 16 tests and executing the code-bearing notebooks sequentially does not establish the absence of the unit, interpretation, or verification errors listed below. The earlier execution check used Python 3.12 with a non-interactive plotting backend; it did not reproduce the Python 3.14.3 environment stated in the README.

## Summary of Corrections

| ID | Affected area | Issue | Status |
|---|---|---|---|
| E01 | Notebook 03, Case 1 | Missing mm–m conversion in the wire-radius sweep and incorrect current-axis unit | Error confirmed · Correction proposed |
| E02 | Notebook 03, Case 3 | Missing mm–m conversion for dielectric thicknesses | Error confirmed · Correction proposed |
| E03 | Notebook 04, Case 3 | Magnetic field and relative error plotted on the same y-axis | Error confirmed · Correction proposed |
| E04 | Notebook 05, Task E | Distance multiplied twice in the inverse-distance verification | Error confirmed · Correction proposed |
| E05 | Notebook 07, Case 2 | Penetration-depth plot data units do not match the axis labels | Error confirmed · Correction proposed |
| E06 | verification.py | Small nonzero reference values classified as zero | Error confirmed · Correction proposed |
| E07 | magnetostatics.py | Requested and actual circular-loop segment counts differ | Error confirmed · Correction proposed |
| E08 | magnetostatics.py | Missing singularity checks for observation points on the line-current path | Error confirmed · Correction proposed |
| E09 | Charge-superposition functions | Some inputs silently ignored when position and charge arrays have different lengths | Confirmed by code inspection · Correction proposed |

## E01. Units in the Wire-Radius Sweep and Current-Axis Label

**Location:** [Notebook 03](../notebooks/03_conductors_currents_and_dielectrics.ipynb), “Case 1: Current and Joule Heating in a Uniform Conducting Wire”  
**Search terms:** `x_1 = np.linspace(0.5, 2.0, 301)`, `uniform_wire_response(voltage_0, L, a_value, sigma)`, `Current $I$`

**Issue:** The radius sweep passes values of 0.5–2.0 directly to the calculation function, while the plot labels the radius in mm. Because the function uses SI length and conductivity, the input radius must also be in m. The current calculation therefore corresponds to radii of 0.5–2.0 m. The current plot also labels its y-axis in V, whereas it should use A.

**Correction:** To retain the intended range of 0.5–2.0 mm, convert to m immediately before calculation.

```python
radius_mm = np.linspace(0.5, 2.0, 301)
radius_m = radius_mm * 1e-3
# Use radius_m for calculations and radius_mm for plots labeled in mm.
```

The separate single-condition input `a = 1.0 * 10**(-4) # [mm]` also needs its value and comment checked for consistency. In the current SI calculation, this value is 1e-4 m, or 0.1 mm. If the intended radius is 0.1 mm, retain the value and correct the comment to `[m]`.

**Impact:** Relative to the intended mm inputs in the sweep, the current resistance is too small by a factor of 1e6, and the current and power are too large by a factor of 1e6. The scaling relationships with radius remain intact, but the absolute values should not be cited as they stand. For fixed voltage, length, and conductivity, the relationships are:

$$R\propto a^{-2},\qquad I\propto a^2,\qquad P\propto a^2.$$

**Reverification criteria:** Compare directly with a reference calculation using a radius of 1 mm expressed in SI units. Confirm that doubling the radius reduces resistance to one quarter and increases current and power fourfold. Update the absolute values in both figures and text after correction.

## E02. Thickness Units in the Layered Capacitor

**Location:** [Notebook 03](../notebooks/03_conductors_currents_and_dielectrics.ipynb), “Case 3: Electric-Field Redistribution Across a Dielectric Interface”  
**Search terms:** `thicknesses = [0.5, 0.5]`, `layered_dielectric_capacitor`

**Issue:** The thicknesses are written as `[0.5, 0.5] # [mm]` but passed without conversion to a calculation function using SI permittivity and area. The calculated thickness of each layer is therefore 0.5 m.

**Correction:** If the intended thickness of each layer is 0.5 mm, pass the values as follows.

```python
thicknesses = np.array([0.5, 0.5]) * 1e-3  # [m]
```

Also choose consistently whether position plots display m or values converted to mm.

**Impact:** For the same applied voltage, area, and relative permittivities, the corrected electric displacement, electric field in each layer, capacitance, and total stored energy will be 1000 times their current values. The voltage drop across each layer and the electric-field ratio remain unchanged. Passing checks on the voltage sum or field ratio therefore cannot, by itself, detect this unit error.

**Reverification criteria:** Confirm that the total thickness is 1e-3 m and compare with the following series-capacitor reference equations.

$$C=\frac{A}{\sum_i d_i/\epsilon_i},\qquad U=\frac12 CV^2.$$

For the current conditions of A = 1e-4 m², V = 10 V, and relative permittivities of 2 and 6, the corrected reference values from these equations are C ≈ 2.6563e-12 F and U ≈ 1.3281e-10 J. These are reference values calculated from the equations, not results from rerunning the complete corrected notebook.

## E03. Mixing Magnetic Field and Relative Error on One Y-Axis

**Location:** [Notebook 04](../notebooks/04_magnetostatic_fields_and_current_sources.ipynb), “Case 3”, “Numerical Experiment: Near Field and Far Field”  
**Search terms:** `Accuracy of the Magnetic Dipole Approximation`, `magnetic_field_exact[sort_index]`, `R_3_sorted * 100`

**Issue:** The exact and dipole-approximation magnetic fields are plotted together with relative error [%] on an axis labeled “Relative Error [%]”. Quantities with different physical dimensions consequently appear on the same scale.

**Correction:** Separate the magnetic-field comparison and relative-error plots. Use T or an explicitly stated normalization for the magnetic-field comparison, and % for the error plot. Place the 5% tolerance line and the reference z/a marker on the error plot.

**Impact:** This is a visualization error. It does not, by itself, invalidate the relative errors or the 5% threshold calculated from the corresponding arrays.

**Reverification criteria:** Confirm that every curve within each plot uses the same y-axis unit.

## E04. Multiplying Distance Twice in the Inverse-Distance Verification

**Location:** [Notebook 05](../notebooks/05_magnetic_forces_and_magnetic_materials.ipynb), “Task E. Inverse-Distance Verification”  
**Search terms:** `F_2_per_L_E = d * I_2`, `scaled_force = d_range * F_L_E_magnitude`

**Issue:** The force per unit length is already multiplied by distance d inside the loop, and then multiplied by d again outside the loop. The calculation evaluates d²(F/L), rather than the intended d(F/L). Its dimensions also differ from those of the reference quantity.

The existing output is:

- `Mean of d(F/L)`: reported as 7.650e-7 N. This unit is incorrect for the quantity actually implemented.
- `Analytical constant`: 3.000e-6 N.
- `Maximum Relative Deviation (E)`: 0.99.

A deviation of 0.99 is 99% and cannot be interpreted as successful verification of the inverse-distance law.

**Correction:** Calculate only F/L inside the loop and multiply by d once outside it. Alternatively, use the force array already calculated in Task D.

```python
scaled_force = d_range * F_L_D_magnitude
analytical_constant = MU_0 * abs(I_1 * I_2) / (2.0 * np.pi)
assert np.allclose(scaled_force, analytical_constant, rtol=1e-12, atol=0.0)
```

**Impact:** The mean, deviation, and verification conclusion in Task E need correction. The preceding magnetic-field and force-magnitude comparisons in A and B, and the attraction/repulsion direction checks, do not use this duplicate multiplication.

**Reverification criteria:** Confirm that d(F/L) agrees with 3.000e-6 N at every distance. In addition to printing the result, include a condition that fails when the tolerance is exceeded. After correction, execute the entire notebook sequentially and update the discussion of the results.

## E05. Axis-Unit Mismatch in the Penetration-Depth Plot

**Location:** [Notebook 07](../notebooks/07_electromagnetic_waves_and_dielectric_interfaces.ipynb), “Case 2: Evanescent Penetration under Total Internal Reflection”  
**Search terms:** `incident_angles_c, penetrate_depth` within `plt.plot(`, `Penetrate Depth versus Incident Angle`

**Issue:** The x data are in rad and the y data are in m, while the axes are labeled deg and μm, respectively.

**Correction:** To retain the axis labels, convert the plotted values as follows.

```python
plt.plot(np.degrees(incident_angles_c), penetrate_depth * 1e6)
plt.xlabel("Incident Angle [deg]")
plt.ylabel("Penetration Depth [μm]")
```

**Impact:** This issue does not change the internal SI calculations of the decay constant or penetration depth. It makes the angular and length scales read from this plot incorrect. The subsequent wavelength–penetration-depth plot already uses `* 1e6` conversions and should be distinguished from this entry.

**Reverification criteria:** Confirm that the internally calculated penetration depth approaches approximately 0.221 μm as the angle approaches 90°, and that the plotted coordinates agree with the printed values. This penetration depth is the 1/e decay length of the field amplitude.

## E06. Classifying Small Nonzero Reference Values as Zero

**Location:** [verification.py](../notebooks/src/verification.py), `relative_error()`  
**Search term:** `np.isclose(reference_value, 0.0)`

**Issue:** The function uses `np.isclose` with its default absolute tolerance to determine whether the reference value is zero. This also rejects small but nonzero physical quantities such as 1e-9.

```python
relative_error(1.01e-9, 1e-9)
# Current behavior: ValueError
# Mathematically defined relative error: approximately 0.01
```

**Correction:** Distinguish actual zero detection from an application-specific threshold for excluding small values. A general relative-error function should handle exactly zero reference values separately. If a lower validity limit for a measurement or calculation is required, accept it as a parameter with explicitly stated units and meaning.

**Impact:** Calls involving small reference values can fail unnecessarily. The same check appears in the relative-error reporting of `find_convergence_threshold()` and the amplitude checks in `phase_error()`, so these should be reviewed together. This does not mean that all currently recorded results are incorrect.

**Reverification criteria:** For nonzero values, confirm that scaling both inputs by the same factor preserves the relative error. Verify the handling of exactly zero reference values separately. Phase is undefined at genuinely zero amplitude, but it is not mathematically undefined merely because the amplitude is small.

## E07. Circular-Loop Segment-Count Mismatch

**Location:** [magnetostatics.py](../notebooks/src/magnetostatics.py), `circular_loop_points()`  
**Search term:** `np.linspace(0.0, 2.0 * np.pi, number_of_segments)`

**Issue:** The function generates N points including both endpoints, so the actual number of consecutive segments is N−1. Passing `number_of_segments=40` produces 39 segments.

**Correction:** If the parameter is to continue meaning the number of segments, generate N+1 points.

```python
phi = np.linspace(0.0, 2.0 * np.pi, number_of_segments + 1)
```

**Impact:** The existing magnetic-field values are approximations based on the N−1 segments actually generated. Descriptions of segment counts and resolution labels in convergence experiments need correction. For example, `circular_loop_points(a, 30, ...)` in Notebook 04 currently uses 29 segments. Because the correction changes the numerical results, existing error values should not be reused unchanged.

**Reverification criteria:** Check `len(points) - 1 == number_of_segments`, closure of the path, preservation of the radius, and the error relative to the analytical solution as the segment count increases.

## E08. Missing Singularity Checks on the Line-Current Path

**Location:** [magnetostatics.py](../notebooks/src/magnetostatics.py), `magnetic_field_line_current()`  
**Search terms:** `segment_midpoints`, `np.isclose(distances, 0.0)`

**Issue:** The function checks only the distance between the observation point and each segment midpoint, so other observation points on a segment are not rejected. The following input currently returns a zero vector even though the observation point lies on the path.

```python
magnetic_field_line_current(
    observation_point=np.array([0.0, 0.0, 0.25]),
    wire_points=np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]]),
    current=1.0,
)
```

**Correction:** Check the shortest distance from the observation point to each finite segment. Use distances to the segment interior or its endpoints so that points are not rejected merely for lying on the infinite extension of a segment. Specify the distance tolerance with attention to the length unit and the scale of the problem.

**Impact:** A finite value returned by this function on the ideal line-current path must not be interpreted as a physical result. This reproduced case does not establish that all existing calculations away from the path are incorrect. For points very close to the path, integration resolution must also be checked separately.

**Reverification criteria:** Confirm that midpoints, other interior points, and endpoints are rejected, while points on the extension beyond a segment are not misclassified as singularities on the path.

## E09. Length Mismatch Between Charge-Position and Charge-Magnitude Arrays

**Location:** `electric_field_multiple_charges()` in [point_charge_electric_field.py](../notebooks/src/point_charge_electric_field.py), and `electric_potential_multiple_charges()` in [electric_potential.py](../notebooks/src/electric_potential.py)  
**Search term:** `zip(charge_positions, charges)`

**Issue:** The functions iterate with `zip` without checking the lengths of the two arrays. If the lengths differ, calculation stops at the end of the shorter array and silently ignores the remaining inputs.

**Correction:** Before superposition, check that the number of positions equals the number of charges, and raise a clearly worded `ValueError` if they differ. Also check dimensional compatibility between the position array and the observation point.

**Impact:** Invalid inputs can produce a result that includes only some of the charges. This entry does not, by itself, invalidate existing notebook results calculated with matching arrays.

**Reverification criteria:** Confirm that valid inputs remain accepted and that inputs containing either one extra charge or one extra position are both rejected.

## Clarifications on Interpretation and Scope

The following entries are distinct from confirmed numerical errors. They clarify the meaning of current functionality or documentation.

### C01. The First Point Within Tolerance Is Not Proof of Convergence

`find_convergence_threshold()` in [verification.py](../notebooks/src/verification.py) returns the first point within tolerance in the supplied array order. It does not check whether subsequent points pass or determine the observed order of convergence.

The output should therefore be interpreted as “the first tested point within tolerance”. It should not be interpreted as guaranteeing convergence beyond that value without inspecting the full error trend. The function can be renamed to reflect this meaning, or supplemented with a separate check of subsequent stability.

### C02. TIR Scope of the Current Fresnel Functions

`snell_angle()` in [optics.py](../notebooks/src/optics.py) raises an exception under TIR conditions, where no real transmitted angle exists. Consequently, `fresnel_coefficients()`, which calls it, does not currently calculate complex TIR reflection coefficients or reflection phases.

The Fresnel sweep in Notebook 07 is performed below the critical angle. Calculating a decay length with the separate `evanescent_decay_constant()` function does not mean that the TIR reflection phase has also been verified. This is a limitation of the current API scope, not an error in the below-critical-angle calculation itself.

### C03. Documentation Structure Described in the README

At the reviewed commit, `docs/project_proposal.md` and `CHECKLIST.md` are empty files. The README should not be read as indicating that all the scope, roadmap, conventions, and errata documents have been written. Adding this document establishes an errata record; it does not complete the other documents.

### C04. What Agreement at Machine Precision Means

Agreement with interference formulas, preservation of the Jones-vector norm, and small residuals in circuit and energy identities support the algebraic consistency of the corresponding calculations. They do not guarantee correct units or input conditions, establish the validity range of approximations, or demonstrate agreement with experiments.

Printing an error must also be distinguished from checking it and failing when a tolerance is exceeded. Expanded tests, CI, and package restructuring are separate improvement tasks and are not prerequisites for completing the corrections in this document.

## Future Updates

When an original file is corrected, add the correction commit, rerun environment, and corrected results to the corresponding ID. Retain the existing errata record and update its status rather than deleting it. If only some numerical results, figures, or text have been updated, state what remains outstanding.
