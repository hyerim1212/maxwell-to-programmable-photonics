import numpy as np
import pytest

from src.waveguide import (
    create_uniform_grid,
    slab_index_profile,
    second_derivative_matrix,
    slab_waveguide_operator,
    solve_eigenmodes,
    select_guided_modes,
)


def solve_reference_waveguide():
    half_domain = 6.0
    grid_spacing = 0.1
    core_width = 4.0

    wavelength_0 = 2.0
    refractive_index_core = 1.5
    refractive_index_cladding = 1.0

    x = create_uniform_grid(
        half_domain,
        grid_spacing,
    )

    number_of_interior_points = len(x) - 2

    refractive_index = slab_index_profile(
        x,
        core_width,
        refractive_index_core,
        refractive_index_cladding,
    )

    second_derivative = second_derivative_matrix(
        number_of_interior_points,
        grid_spacing,
    )

    operator = slab_waveguide_operator(
        second_derivative,
        refractive_index[1:-1],
        wavelength_0,
    )

    eigenvalues, eigenvectors = solve_eigenmodes(
        operator
    )

    return select_guided_modes(
        eigenvalues,
        eigenvectors,
        wavelength_0,
        refractive_index_core,
        refractive_index_cladding,
    )


def test_reference_waveguide_has_five_guided_modes():
    _, _, guided_effective_indices = (
        solve_reference_waveguide()
    )

    assert len(guided_effective_indices) == 5


def test_guided_effective_indices_lie_between_material_indices():
    _, _, guided_effective_indices = (
        solve_reference_waveguide()
    )

    assert np.all(guided_effective_indices > 1.0)
    assert np.all(guided_effective_indices < 1.5)


def test_fundamental_mode_matches_analytical_reference():
    _, _, guided_effective_indices = (
        solve_reference_waveguide()
    )

    numerical_neff_TE0 = guided_effective_indices[0]

    analytical_neff_TE0 = 1.4839755723

    assert numerical_neff_TE0 == pytest.approx(
        analytical_neff_TE0,
        rel=1e-3,
    )