
import numpy as np
import pytest
from scipy.integrate import solve_ivp

from src.coupler import (
    coupled_mode_rhs,
    coupled_mode_transfer,
    double_slab_cell_average,
)

from src.waveguide import (
    create_uniform_grid,
    second_derivative_matrix,
    slab_waveguide_operator,
    solve_eigenmodes,
    select_guided_modes,
)

from src.verification import complex_error


# ============================================================
# Case 1 — Two-Mode Coupled-Mode Theory
# ============================================================

@pytest.mark.parametrize("kappa", [0.0, 0.4, 1.0])
def test_analytic_solution(kappa):
    """Compare matrix exponential with the analytical solution."""

    H = np.array([
        [0.0, kappa],
        [kappa, 0.0]
    ], dtype=complex)

    a0 = np.array([1.0, 0.0], dtype=complex)
    z_values = np.linspace(0.0, 3.0, 21)

    numerical = np.array([
        coupled_mode_transfer(H, z) @ a0
        for z in z_values
    ])

    analytical = np.column_stack((
        np.cos(kappa * z_values),
        -1j * np.sin(kappa * z_values)
    ))

    error = complex_error(numerical, analytical)

    assert np.max(error) < 1e-12


def test_power_conservation():
    """Total modal power must be conserved in a lossless coupler."""

    kappa = 1.0

    H = np.array([
        [0.0, kappa],
        [kappa, 0.0]
    ], dtype=complex)

    a0 = np.array([1.0, 2.0j], dtype=complex)
    a0 = a0 / np.linalg.norm(a0)

    z_values = np.linspace(0.0, 10.0, 31)

    for z in z_values:
        a = coupled_mode_transfer(H, z) @ a0

        total_power = np.sum(np.abs(a)**2)

        assert total_power == pytest.approx(
            1.0, abs=1e-12
        )


def test_ode_agreement():
    """Compare solve_ivp with the matrix exponential solution."""

    kappa = 1.0

    H = np.array([
        [0.0, kappa],
        [kappa, 0.0]
    ], dtype=complex)

    a0 = np.array([1.0, 0.0], dtype=complex)
    z_values = np.linspace(0.0, np.pi, 51)

    solution = solve_ivp(
        coupled_mode_rhs,
        t_span=(z_values[0], z_values[-1]),
        y0=a0,
        t_eval=z_values,
        args=(H,),
        rtol=1e-9,
        atol=1e-12,
    )

    assert solution.success

    reference = np.array([
        coupled_mode_transfer(H, z) @ a0
        for z in z_values
    ])

    error = complex_error(solution.y.T, reference)

    assert np.max(error) < 1e-7


# ============================================================
# Case 2 — Double-Slab Supermodes
# ============================================================

def _solve_double_slab(gap):
    """
    Compute the two guided supermodes of a symmetric
    double-slab waveguide.

    Uses a reduced grid for fast regression testing.
    """

    half_domain = 4.0
    grid_spacing = 0.05
    core_width = 0.8

    wavelength_0 = 2.0
    n_core = 1.5
    n_clad = 1.0

    x = create_uniform_grid(
        half_domain, grid_spacing
    )

    dx = x[1] - x[0]

    n, core_fraction = double_slab_cell_average(
        x, core_width, gap, n_core, n_clad
    )

    D = second_derivative_matrix(
        len(x) - 2, dx
    )

    A = slab_waveguide_operator(
        D, n[1:-1], wavelength_0
    )

    eigenvalues, eigenvectors = solve_eigenmodes(A)

    _, guided_modes, guided_neff = select_guided_modes(
        eigenvalues,
        eigenvectors,
        wavelength_0,
        n_core,
        n_clad,
    )

    if len(guided_neff) != 2:
        raise AssertionError(
            f"Expected 2 guided supermodes, "
            f"found {len(guided_neff)}"
        )

    k0 = 2 * np.pi / wavelength_0
    beta = k0 * guided_neff

    kappa_eff = abs(beta[0] - beta[1]) / 2

    return {
        "x": x,
        "n": n,
        "core_fraction": core_fraction,
        "modes": guided_modes,
        "neff": guided_neff,
        "beta": beta,
        "kappa": kappa_eff,
    }


@pytest.fixture(scope="module")
def reference_supermodes():
    """Shared reference computation at gap = 0.5 um."""
    return _solve_double_slab(gap=0.5)


def test_double_slab_geometry():
    """Verify symmetry and represented core width."""

    x = create_uniform_grid(4.0, 0.05)
    dx = x[1] - x[0]

    n, fraction = double_slab_cell_average(
        x,
        width=0.8,
        gap=0.5,
        n_core=1.5,
        n_clad=1.0,
    )

    np.testing.assert_allclose(
        n, n[::-1], atol=1e-12, rtol=0
    )

    assert np.all(fraction >= -1e-12)
    assert np.all(fraction <= 1.0 + 1e-12)

    represented_width = np.sum(fraction) * dx

    assert represented_width == pytest.approx(
        2 * 0.8, abs=1e-12
    )

    assert np.all(n >= 1.0 - 1e-12)
    assert np.all(n <= 1.5 + 1e-12)


def test_supermode_splitting(reference_supermodes):
    """Verify parity, guided bounds, and mode splitting."""

    result = reference_supermodes

    neff = result["neff"]
    modes = result["modes"]
    beta = result["beta"]
    kappa_eff = result["kappa"]

    assert np.all(neff > 1.0)
    assert np.all(neff < 1.5)

    assert beta[0] > beta[1]

    psi_even = modes[:, 0]
    psi_odd = modes[:, 1]

    even_residual = (
        np.linalg.norm(psi_even - psi_even[::-1])
        / np.linalg.norm(psi_even)
    )

    odd_residual = (
        np.linalg.norm(psi_odd + psi_odd[::-1])
        / np.linalg.norm(psi_odd)
    )

    assert even_residual < 1e-8
    assert odd_residual < 1e-8

    assert kappa_eff > 0.0

    # Grid-specific regression reference, not an analytic value.
    assert kappa_eff == pytest.approx(
        0.088257, rel=0.03
    )

    coupling_length = np.pi / (2 * kappa_eff)
    assert np.isfinite(coupling_length)
    assert coupling_length > 0.0


def test_gap_dependence():
    """Coupling must decrease with gap in this parameter regime."""

    small_gap = _solve_double_slab(gap=0.35)
    large_gap = _solve_double_slab(gap=0.75)

    kappa_small = small_gap["kappa"]
    kappa_large = large_gap["kappa"]

    assert kappa_small > kappa_large > 0.0

    Lc_small = np.pi / (2 * kappa_small)
    Lc_large = np.pi / (2 * kappa_large)

    assert Lc_large > Lc_small


# ============================================================
# Case 3 — Supermode Reconstruction
# ============================================================

def test_supermode_reconstruction(reference_supermodes):
    """
    Compare spatial supermode reconstruction with
    two-mode CMT in the localized-mode basis.
    """

    result = reference_supermodes

    x_int = result["x"][1:-1]
    modes = result["modes"]
    beta_even, beta_odd = result["beta"]
    kappa = result["kappa"]

    psi_even = modes[:, 0].copy()
    psi_odd = modes[:, 1].copy()

    # Fix the relative eigenvector sign convention.
    if np.dot(
        psi_even[x_int > 0],
        psi_odd[x_int > 0]
    ) < 0:
        psi_odd = -psi_odd

    phi_R = (psi_even + psi_odd) / np.sqrt(2)
    phi_L = (psi_even - psi_odd) / np.sqrt(2)

    # Orthogonality of the localized-mode basis.
    assert abs(np.vdot(phi_R, phi_L)) < 1e-10

    Lc = np.pi / (2 * kappa)
    z_values = np.linspace(0.0, 2 * Lc, 21)

    # Spatial field reconstruction.
    E = (
        np.exp(-1j * beta_even * z_values[:, None])
        * psi_even
        +
        np.exp(-1j * beta_odd * z_values[:, None])
        * psi_odd
    ) / np.sqrt(2)

    # Projection onto localized modes.
    a_R = E @ np.conj(phi_R)
    a_L = E @ np.conj(phi_L)

    beta_mean = (beta_even + beta_odd) / 2
    phase = np.exp(1j * beta_mean * z_values)

    reconstructed = np.column_stack((
        phase * a_R,
        phase * a_L
    ))

    # CMT reference in the same phase convention.
    H = np.array([
        [0.0, kappa],
        [kappa, 0.0]
    ], dtype=complex)

    a0 = np.array([1.0, 0.0], dtype=complex)

    reference = np.array([
        coupled_mode_transfer(H, z) @ a0
        for z in z_values
    ])

    error = complex_error(reconstructed, reference)

    assert np.max(error) < 1e-10

    # Conservation of the discrete field norm.
    field_norm = np.sum(np.abs(E)**2, axis=1)

    np.testing.assert_allclose(
        field_norm,
        np.ones_like(z_values),
        atol=1e-10,
        rtol=0,
    )
