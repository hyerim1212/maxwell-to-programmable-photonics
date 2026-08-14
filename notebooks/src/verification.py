import numpy as np

def relative_residual(reference, comparison):
    reference, comparison = np.broadcast_arrays(
        np.asarray(reference, dtype=float),
        np.asarray(comparison, dtype=float)
    )

    residual = np.empty(reference.shape, dtype=float)

    nonzero_mask = reference != 0

    residual[nonzero_mask] = (
        np.abs(comparison[nonzero_mask] - reference[nonzero_mask])
        / np.abs(reference[nonzero_mask])
    )

    residual[~nonzero_mask] = np.where(
        comparison[~nonzero_mask] == 0,
        0.0,
        np.inf
    )

    if residual.ndim == 0:
        return float(residual)

    return residual

def absolute_error(numerical_value: float | np.ndarray, reference_value: float | np.ndarray,) -> float | np.ndarray:
    
    numerical_value = np.asarray(numerical_value, dtype=float)
    reference_value = np.asarray(reference_value, dtype=float)

    if not np.all(np.isfinite(numerical_value)):
        raise ValueError(
            "numerical_value must contain only finite values."
        )

    if not np.all(np.isfinite(reference_value)):
        raise ValueError(
            "reference_value must contain only finite values."
        )

    try:
        error = np.abs(numerical_value - reference_value)
    except ValueError as exc:
        raise ValueError(
            "numerical_value and reference_value must have "
            "compatible shapes."
        ) from exc

    if error.ndim == 0:
        return float(error)

    return error

def relative_error(numerical_value: float | np.ndarray, reference_value: float | np.ndarray,) -> float | np.ndarray:

    numerical_value = np.asarray(numerical_value, dtype=float)
    reference_value = np.asarray(reference_value, dtype=float)

    if not np.all(np.isfinite(numerical_value)):
        raise ValueError("numerical_value must contain only finite values.")

    if not np.all(np.isfinite(reference_value)):
        raise ValueError("reference_value must contain only finite values.")

    if np.any(np.isclose(reference_value, 0.0)):
        raise ValueError("relative error is undefined when reference_value is zero. Use absolute_error or is_within_tolerance instead.")

    try:
        error = (np.abs(numerical_value - reference_value) / np.abs(reference_value))
        
    except ValueError as exc:
        raise ValueError("numerical_value and reference_value must have compatible shapes.") from exc

    if error.ndim == 0:
        return float(error)

    return error


def is_within_tolerance(numerical_value: float | np.ndarray, reference_value: float | np.ndarray,
    relative_tolerance: float = 1e-5, absolute_tolerance: float = 0.0,) -> bool | np.ndarray:
    
    if not np.isfinite(relative_tolerance):
        raise ValueError("relative_tolerance must be finite.")

    if not np.isfinite(absolute_tolerance):
        raise ValueError("absolute_tolerance must be finite.")

    if relative_tolerance < 0.0:
        raise ValueError("relative_tolerance must be nonnegative.")

    if absolute_tolerance < 0.0:
        raise ValueError("absolute_tolerance must be nonnegative.")

    numerical_value = np.asarray(numerical_value, dtype=float)
    reference_value = np.asarray(reference_value, dtype=float)

    if not np.all(np.isfinite(numerical_value)):
        raise ValueError("numerical_value must contain only finite values.")

    if not np.all(np.isfinite(reference_value)):
        raise ValueError("reference_value must contain only finite values.")

    try:
        error = np.abs(numerical_value - reference_value)
        allowed_error = (absolute_tolerance + relative_tolerance * np.abs(reference_value))
        result = error <= allowed_error
        
    except ValueError as exc:
        raise ValueError(
            "numerical_value and reference_value must have "
            "compatible shapes.") from exc

    if result.ndim == 0:
        return bool(result)

    return result


def find_convergence_threshold(parameter_values: np.ndarray, numerical_values: np.ndarray, reference_value: float,
    relative_tolerance: float = 1e-5, absolute_tolerance: float = 0.0) -> dict | None:

    parameter_values = np.asarray(parameter_values)
    numerical_values = np.asarray(numerical_values, dtype=float)

    if parameter_values.ndim != 1:
        raise ValueError("parameter_values must be one-dimensional.")

    if numerical_values.ndim != 1:
        raise ValueError("numerical_values must be one-dimensional.")

    if len(parameter_values) != len(numerical_values):
        raise ValueError(
            "parameter_values and numerical_values must have "
            "the same length.")

    if len(parameter_values) == 0:
        raise ValueError("parameter_values and numerical_values must not be empty.")

    if not np.all(np.isfinite(parameter_values)):
        raise ValueError("parameter_values must contain only finite values.")

    if not np.all(np.isfinite(numerical_values)):
        raise ValueError("numerical_values must contain only finite values.")

    if not np.isscalar(reference_value):
        raise ValueError("reference_value must be a scalar.")

    reference_value = float(reference_value)

    if not np.isfinite(reference_value):
        raise ValueError("reference_value must be finite.")

    accepted = is_within_tolerance(numerical_value=numerical_values, reference_value=reference_value,
        relative_tolerance=relative_tolerance, absolute_tolerance=absolute_tolerance)

    accepted_indices = np.flatnonzero(accepted)

    if accepted_indices.size == 0:
        return None

    index = int(accepted_indices[0])
    numerical_value = float(numerical_values[index])
    absolute_error_value = float(absolute_error(numerical_value, reference_value))

    if np.isclose(reference_value, 0.0):
        relative_error_value = None
    else:
        relative_error_value = float(
            relative_error(numerical_value, reference_value))

    parameter_value = parameter_values[index]

    if isinstance(parameter_value, np.generic):
        parameter_value = parameter_value.item()

    return {
        "parameter_value": parameter_value,
        "numerical_value": numerical_value,
        "reference_value": reference_value,
        "absolute_error": absolute_error_value,
        "relative_error": relative_error_value,
        "index": index,
    }


def power_conservation_error(reflectance: float | np.ndarray, transmittance: float | np.ndarray,
) -> float | np.ndarray:
    
    return abs(reflectance + transmittance - 1.0)