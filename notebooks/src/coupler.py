# for test


import numpy as np
from scipy.linalg import expm


def coupled_mode_rhs(z, a, H):
    """Two-mode coupled-mode differential equation."""
    return -1j * (H @ a)


def coupled_mode_transfer(H, z):
    """Transfer matrix for a constant coupling Hamiltonian."""
    return expm(-1j * H * z)


def double_slab_cell_average(x, width, gap, n_core, n_clad):
    """
    Construct a symmetric double-slab index profile
    using cell-averaged relative permittivity.
    """
    dx = x[1] - x[0]
    c = (width + gap) / 2

    cell_left = x - dx / 2
    cell_right = x + dx / 2

    core_fraction = np.zeros_like(x, dtype=float)

    core_intervals = [
        (-c - width / 2, -c + width / 2),
        ( c - width / 2,  c + width / 2),
    ]

    for a, b in core_intervals:
        overlap = np.maximum(
            0.0,
            np.minimum(cell_right, b)
            - np.maximum(cell_left, a)
        )
        core_fraction += overlap / dx

    eps_r = (
        n_clad**2
        + core_fraction * (n_core**2 - n_clad**2)
    )

    return np.sqrt(eps_r), core_fraction
