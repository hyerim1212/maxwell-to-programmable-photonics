import numpy as np


def coupler_matrix(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -1j * s],
        [-1j * s, c]
    ], dtype=complex)


def phase_matrix(phi):
    return np.diag([1, np.exp(1j * phi)]).astype(complex)


def mzi_matrix(theta_1, theta_2, phi):
    return (
        coupler_matrix(theta_2)
        @ phase_matrix(phi)
        @ coupler_matrix(theta_1)
    )
