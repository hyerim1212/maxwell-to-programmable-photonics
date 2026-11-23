import numpy as np

from .mzi import (coupler_matrix,phase_matrix, mzi_matrix,)


def programmable_matrix(alpha, phi, beta):
    ##Ideal programmable 2x2 MZI.
    theta = np.pi / 4

    return (phase_matrix(alpha) @ mzi_matrix(theta, theta, phi) @ phase_matrix(beta))


def synthesize_phases_new(U_target, tol=1e-12):
    ### Synthesize a unitary target up to global phase.
    U_target = np.asarray(U_target, dtype=complex)

    if U_target.shape != (2, 2):
        raise ValueError("Target must be a 2x2 matrix.")

    I = np.eye(2, dtype=complex)

    if (
        not np.all(np.isfinite(U_target))
        or not np.allclose(
            U_target.conj().T @ U_target,
            I,
            atol=tol,
            rtol=0,
        )
    ):
        raise ValueError("Target must be unitary.")

    if np.abs(U_target[0, 0]) < tol:
        # Off-diagonal transformation
        alpha = np.angle(
            U_target[1, 0] / U_target[0, 1]
        )
        phi = 0.0
        beta = 0.0

    elif np.abs(U_target[0, 1]) < tol:
        # Diagonal transformation
        alpha = np.angle(
            -U_target[1, 1] / U_target[0, 0]
        )
        phi = np.pi
        beta = 0.0

    else:
        # General transformation
        alpha = np.angle(
            U_target[1, 0] / U_target[0, 0]
        )
        beta = np.angle(
            U_target[0, 1] / U_target[0, 0]
        )
        phi = 2 * np.arctan2(
            np.abs(U_target[0, 0]),
            np.abs(U_target[0, 1]),
        )

    return alpha, phi, beta
    
def lossy_programmable_matrix(alpha, phi, beta, eta1, eta2):
   
    for eta in (eta1, eta2):
        if (
            not np.isscalar(eta)
            or not np.isrealobj(eta)
            or not np.isfinite(eta)
            or not (0 <= eta <= 1)
        ):
            raise ValueError(
                "Arm power transmission must be "
                "finite and within [0, 1]."
            )

    C = coupler_matrix(np.pi / 4)

    L = np.diag([
        np.sqrt(eta1),
        np.sqrt(eta2),
    ])

    return (phase_matrix(alpha) @ C @ phase_matrix(phi) @ L @ C @ phase_matrix(beta))
