import numpy as np

epsilon_0 = 8.8541878128e-12
K_e = 1.0 / (4.0 * np.pi * epsilon_0)

MU_0 = 4*np.pi*10e-7 #[H/m]

def magnetic_field_line_current(observation_point: np.ndarray, wire_points: np.ndarray, current: float,) -> np.ndarray :

    observation_point = np.asarray(observation_point, dtype=float)
    wire_points = np.asarray(wire_points, dtype=float)

    if observation_point.shape != (3,):
        raise ValueError("observation_point must have shape (3,).")

    if wire_points.ndim != 2 or wire_points.shape[1] != 3:
        raise ValueError("wire_points must have shape (N, 3).")

    if len(wire_points) < 2:
        raise ValueError("wire_points must contain at least two points.")

    if not np.all(np.isfinite(observation_point)):
        raise ValueError("observation_point must contain only finite values.")

    if not np.all(np.isfinite(wire_points)):
        raise ValueError("wire_points must contain only finite values.")

    if not np.isfinite(current):
        raise ValueError("current must be finite.")

    segment_vectors = wire_points[1:] - wire_points[:-1] 
    segment_lengths = np.linalg.norm(segment_vectors,axis=1)

    if np.any(np.isclose(segment_lengths, 0.0)):
        raise ValueError("Consecutive wire points must not coincide.")

    segment_midpoints = 0.5 * (wire_points[1:] + wire_points[:-1])

    displacements = (observation_point[None, :]- segment_midpoints)
    distances = np.linalg.norm(displacements, axis=1)

    if np.any(np.isclose(distances, 0.0)):
        raise ValueError("The magnetic field is singular on the line-current path.")

    cross_products = np.cross(segment_vectors, displacements)
    contributions = (cross_products / distances[:, None] ** 3)

    magnetic_field = ( MU_0 * current / (4.0 * np.pi) * np.sum(contributions, axis=0))

    return magnetic_field

def circular_loop_points(radius: float, number_of_segments: int, center: np.ndarray | None = None,
                         normal_axis: str = "z") -> np.ndarray:
    if radius <= 0:
        raise ValueError("radius must be positive.")

    if number_of_points < 4:
        raise ValueError("number_of_points must be at least 4.")

    if center is None:
        center = np.zeros(3)

    center = np.asarray(center, dtype=float)

    if center.shape != (3,):
        raise ValueError(
            "center must have shape (3,).")

    if normal_axis not in {"x", "y", "z"}:
        raise ValueError(
            "normal_axis must be 'x', 'y', or 'z'.")

    phi = np.linspace(0.0, 2.0 * np.pi, number_of_segments)

    cosine = radius * np.cos(phi)
    sine = radius * np.sin(phi)
    zeros = np.zeros_like(phi)

    if normal_axis == "z":
        relative_points = np.column_stack([cosine ,sine, zeros])

    elif normal_axis == "x":
        relative_points = np.column_stack([zeros, cosine, sine])

    else:
        relative_points = np.column_stack([cosine, zeros, sine])

    return relative_points + center


def magnetic_field_infinite_straight_wire(observation_point: np.ndarray, current: float, wire_point: np.ndarray | None = None, wire_direction: np.ndarray | None = None,) -> np.ndarray:

    observation_point = np.asarray(observation_point, dtype=float)

    if wire_point is None:
        wire_point = np.zeros(3)
    else:
        wire_point = np.asarray(wire_point,dtype=float,)

    if wire_direction is None:
        wire_direction = np.array([0.0, 0.0, 1.0,])
    else:
        wire_direction = np.asarray(wire_direction, dtype=float)

    if observation_point.shape != (3,):
        raise ValueError("observation_point must have shape (3,).")

    if wire_point.shape != (3,):
        raise ValueError("wire_point must have shape (3,).")

    if wire_direction.shape != (3,):
        raise ValueError("wire_direction must have shape (3,).")

    if not np.all(np.isfinite(observation_point)):
        raise ValueError("observation_point must contain only finite values.")

    if not np.all(np.isfinite(wire_point)):
        raise ValueError("wire_point must contain only finite values.")

    if not np.all(np.isfinite(wire_direction)):
        raise ValueError("wire_direction must contain only finite values.")

    if not np.isfinite(current):
        raise ValueError("current must be finite.")

    direction_norm = np.linalg.norm(wire_direction)

    if np.isclose(direction_norm, 0.0):
        raise ValueError("wire_direction must be nonzero.")

    direction_unit = (wire_direction / direction_norm)

    displacement = (observation_point - wire_point)

    parallel_displacement = (np.dot(displacement, direction_unit)* direction_unit)

    radial_displacement = (displacement - parallel_displacement)

    radial_distance = np.linalg.norm(radial_displacement)

    if np.isclose(radial_distance, 0.0):
        raise ValueError("The magnetic field is singular on the wire.")

    radial_unit = (radial_displacement / radial_distance)

    magnetic_field_direction = np.cross(direction_unit, radial_unit,)

    magnetic_field = (MU_0 * current / (2.0 * np.pi * radial_distance) * magnetic_field_direction)

    return magnetic_field


def magnetic_field_circular_loop_axis(axial_position, radius: float, current: float,) -> np.ndarray:
    
    observation_point = np.asarray(observation_point, dtype=float,)

    if center is None:
        center = np.zeros(3)
    else:
        center = np.asarray(center, dtype=float)

    
    if normal_direction is None:
        normal_direction = np.array([0.0, 0.0, 1.0])
    else:
        normal_direction = np.asarray(normal_direction, dtype=float)

    if observation_point.shape != (3,):
        raise ValueError("observation_point must have shape (3,).")

    if center.shape != (3,):
        raise ValueError("center must have shape (3,).")

    if normal_direction.shape != (3,):
        raise ValueError("normal_direction must have shape (3,).")

    if not np.all(np.isfinite(observation_point)):
        raise ValueError("observation_point must contain only finite values.")

    if not np.all(np.isfinite(center)):
        raise ValueError("center must contain only finite values.")

    if not np.all(np.isfinite(normal_direction)):
        raise ValueError("normal_direction must contain only finite values.")

    if not np.isfinite(radius):
        raise ValueError("radius must be finite.")

    if radius <= 0.0:
        raise ValueError("radius must be positive.")

    if not np.isfinite(current):
        raise ValueError("current must be finite.")

    normal_magnitude = np.linalg.norm(normal_direction)

    if np.isclose(normal_magnitude, 0.0):
        raise ValueError("normal_direction must be nonzero.")

    normal_unit = (normal_direction / normal_magnitude)

    displacement = (observation_point - center)

    axial_position = np.dot(displacement, normal_unit)

    axial_displacement = (axial_position * normal_unit)

    radial_displacement = (displacement - axial_displacement)

    radial_distance = np.linalg.norm(radial_displacement)

    if not np.isclose(radial_distance, 0.0):
        raise ValueError(
            "observation_point must lie on the symmetry axis "
            "of the circular loop.")

    magnetic_field_magnitude = (MU_0* current* radius**2/ (2.0* (radius**2 + axial_position**2) ** 1.5))

    magnetic_field = (magnetic_field_magnitude* normal_unit)

    return magnetic_field