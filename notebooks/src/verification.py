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