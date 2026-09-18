from scipy.linalg import eigh
import numpy as np

def create_uniform_grid(half_domain: float, grid_spacing: float) -> np.ndarray:

    N_total = round(2 * half_domain / grid_spacing) + 1

    x = np.linspace( -half_domain,half_domain, N_total)

    return x
    
def slab_index_profile(x: np.ndarray, core_width: float, refractive_index_core: float, refractive_index_cladding: float) -> np.ndarray:
                       
    core_region = np.abs(x) <= core_width / 2

    refractive_index_profile = np.full(x.shape, refractive_index_cladding, dtype = float)
    refractive_index_profile[core_region] = refractive_index_core

    return refractive_index_profile

def second_derivative_matrix(number_of_interior_points: int, grid_spacing: float) -> np.ndarray:

    main_diag = -2.0 * np.ones(number_of_interior_points)
    off_diag = np.ones(number_of_interior_points - 1)
    D = (np.diag(main_diag) + np.diag(off_diag, -1) + np.diag(off_diag, 1))/ grid_spacing ** 2

    return D

def slab_waveguide_operator(second_derivative: np.ndarray, refractive_index: np.ndarray, wavelength_0: float,) -> np.ndarray:

    k_0 = 2 * np.pi / wavelength_0
    
    n_squared_diag = np.diag(refractive_index**2)

    A = second_derivative + ((k_0)**2) * n_squared_diag

    return A

def solve_eigenmodes(operator: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    
    eigenvalues, eigenvectors = eigh(operator)

    return eigenvalues, eigenvectors

def select_guided_modes(eigenvalues: np.ndarray,eigenvectors: np.ndarray,
    wavelength_0: float, refractive_index_core: float, refractive_index_cladding: float,) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    k_0 = 2 * np.pi / wavelength_0

    lower_bound = (k_0 * refractive_index_cladding) ** 2
    upper_bound = (k_0 * refractive_index_core) ** 2

    guided_mask = (
        (eigenvalues > lower_bound)
        & (eigenvalues < upper_bound)
    )

    guided_eigenvalues = eigenvalues[guided_mask]
    guided_eigenvectors = eigenvectors[:, guided_mask]

    guided_eigenvalues = guided_eigenvalues[::-1]
    guided_eigenvectors = guided_eigenvectors[:, ::-1]

    guided_effective_indices = (
        np.sqrt(guided_eigenvalues) / k_0
    )

    return (
        guided_eigenvalues,
        guided_eigenvectors,
        guided_effective_indices,
    )