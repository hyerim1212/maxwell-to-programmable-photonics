
# tests/test_programmable.py

import numpy as np
import pytest

from src.mzi import mzi_matrix
from src.programmable import (
    programmable_matrix,
    synthesize_phases_new,
    lossy_programmable_matrix,
)


TOL = 1e-12

COMPLEX_TARGET = np.array([
    [1, np.exp(1j * np.pi / 3)],
    [
        np.exp(1j * np.pi / 4),
        -np.exp(1j * 7 * np.pi / 12),
    ],
], dtype=complex) / np.sqrt(2)


def reconstruction_error(U, target):
    """Relative Frobenius error after global-phase alignment."""
    overlap = np.trace(target.conj().T @ U)
    chi = np.angle(overlap)

    return (
        np.linalg.norm(
            np.exp(-1j * chi) * U - target,
            ord="fro",
        )
        / np.linalg.norm(target, ord="fro")
    )


# ============================================================
# Case 1 — Unitarity and Target Synthesis
# ============================================================

@pytest.mark.parametrize(
    "theta1,theta2,phi",
    [
        (np.pi / 4, np.pi / 4, 0.0),
        (np.pi / 4, np.pi / 4, np.pi / 2),
        (0.40, 0.70, np.pi),
        (0.30, 0.90, 1.20),
    ],
)
def test_mzi_unitarity(theta1, theta2, phi):
    U = mzi_matrix(theta1, theta2, phi)

    np.testing.assert_allclose(
        U.conj().T @ U,
        np.eye(2),
        atol=TOL,
        rtol=0,
    )


@pytest.mark.parametrize(
    "target",
    [
        pytest.param(
            np.eye(2, dtype=complex),
            id="identity",
        ),
        pytest.param(
            np.array([[0, 1], [1, 0]], dtype=complex),
            id="swap",
        ),
        pytest.param(
            COMPLEX_TARGET,
            id="complex-unitary",
        ),
    ],
)
def test_target_reconstruction(target):
    alpha, phi, beta = synthesize_phases_new(target)

    U = programmable_matrix(alpha, phi, beta)

    assert reconstruction_error(U, target) < TOL


def test_random_unitary_reconstruction():
    """Check additional non-boundary unitary targets."""
    rng = np.random.default_rng(2026)

    for _ in range(10):
        A = (
            rng.standard_normal((2, 2))
            + 1j * rng.standard_normal((2, 2))
        )

        target, _ = np.linalg.qr(A)

        phases = synthesize_phases_new(target)
        U = programmable_matrix(*phases)

        assert reconstruction_error(U, target) < TOL


# ============================================================
# Case 2 — Reachability Bounds
# ============================================================

@pytest.mark.parametrize(
    "g1,g2",
    [
        (0.50, 0.50),
        (0.55, 0.55),
        (0.55, 0.45),
    ],
)
def test_reachability_bounds(g1, g2):
    g0 = 0.5
    kappa0 = 0.088084729155
    gamma = 2.738058478476613

    L_DC = np.pi / (4 * kappa0)

    theta1 = (
        kappa0 * np.exp(-gamma * (g1 - g0)) * L_DC
    )
    theta2 = (
        kappa0 * np.exp(-gamma * (g2 - g0)) * L_DC
    )

    P_min = np.cos(theta1 + theta2)**2
    P_max = np.cos(theta1 - theta2)**2

    # Exact analytical extrema occur at phi = 0 and pi.
    P_at_zero = np.abs(
        mzi_matrix(theta1, theta2, 0.0)[0, 0]
    )**2

    P_at_pi = np.abs(
        mzi_matrix(theta1, theta2, np.pi)[0, 0]
    )**2

    assert P_at_zero == pytest.approx(
        P_min, abs=TOL
    )
    assert P_at_pi == pytest.approx(
        P_max, abs=TOL
    )

    # Check that the entire sampled curve stays in range.
    for phi in np.linspace(0, 2 * np.pi, 65):
        P = np.abs(
            mzi_matrix(theta1, theta2, phi)[0, 0]
        )**2

        assert P_min - TOL <= P <= P_max + TOL


# ============================================================
# Case 3 — Optical Loss
# ============================================================

@pytest.mark.parametrize(
    "eta1,eta2",
    [
        (0.65, 0.65),
        (0.90, 0.40),
    ],
)
def test_lossy_fidelity_and_transmission(eta1, eta2):
    alpha = np.pi / 4
    phi = np.pi / 2
    beta = np.pi / 3

    U = lossy_programmable_matrix(
        alpha, phi, beta, eta1, eta2
    )

    trace_power = np.trace(U.conj().T @ U).real

    T_numerical = trace_power / 2

    F_numerical = (
        np.abs(np.trace(COMPLEX_TARGET.conj().T @ U))**2
        / (2 * trace_power)
    )

    T_analytical = (eta1 + eta2) / 2

    F_analytical = (
        (np.sqrt(eta1) + np.sqrt(eta2))**2
        / (2 * (eta1 + eta2))
    )

    assert T_numerical == pytest.approx(
        T_analytical, abs=TOL
    )
    assert F_numerical == pytest.approx(
        F_analytical, abs=TOL
    )


@pytest.mark.parametrize(
    "eta1,eta2,expected",
    [
        (0.65, 0.65, [0.65, 0.65, 0.65]),
        (0.90, 0.40, [0.65, 0.90, 0.40]),
    ],
)
def test_input_dependent_transmission(
    eta1, eta2, expected
):
    alpha = np.pi / 4
    phi = np.pi / 2
    beta = np.pi / 3

    U = lossy_programmable_matrix(
        alpha, phi, beta, eta1, eta2
    )

    inputs = [
        np.array([1, 0], dtype=complex),

        np.array([
            1, 1j * np.exp(-1j * beta)
        ]) / np.sqrt(2),

        np.array([
            1, -1j * np.exp(-1j * beta)
        ]) / np.sqrt(2),
    ]

    for a_in, expected_T in zip(inputs, expected):
        a_out = U @ a_in

        T = (
            np.vdot(a_out, a_out).real
            / np.vdot(a_in, a_in).real
        )

        assert T == pytest.approx(
            expected_T, abs=TOL
        )


# ============================================================
# Invalid Inputs
# ============================================================

@pytest.mark.parametrize(
    "target",
    [
        np.eye(3),
        np.diag([1.0, 0.9]),
        np.array([
            [1.0, np.nan],
            [0.0, 1.0],
        ]),
    ],
)
def test_invalid_target_rejected(target):
    with pytest.raises(ValueError):
        synthesize_phases_new(target)


@pytest.mark.parametrize(
    "eta1,eta2",
    [
        (-0.1, 0.5),
        (0.5, 1.1),
        (np.nan, 0.5),
        (0.5, np.inf),
    ],
)
def test_invalid_loss_rejected(eta1, eta2):
    with pytest.raises(ValueError):
        lossy_programmable_matrix(
            np.pi / 4,
            np.pi / 2,
            np.pi / 3,
            eta1,
            eta2,
        )
