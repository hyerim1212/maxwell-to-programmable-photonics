import numpy as np

epsilon_0 = 8.8541878128e-12
K_e = 1.0 / (4.0 * np.pi * epsilon_0)

def electric_potential_point_charge(observation_point: np.ndarray, charge_position: np.ndarray, charge: float) -> float:
    displacement = observation_point - charge_position
    distance = np.linalg.norm(displacement)

    if np.isclose(distance, 0.0):
        raise ValueError("The electric potential is undefined at the charge position.")

    return K_e * charge / distance


def electric_potential_multiple_charges(observation_point: np.ndarray, charge_positions: np.ndarray, charges: np.ndarray) -> float:
    potential = 0.0

    for position, charge in zip(charge_positions, charges):
        potential += electric_potential_point_charge(observation_point, position, charge)

    return potential

def electrostatic_potential_energy(charge_positions: np.ndarray ,charges: np.ndarray):
    energy = 0
    number = len(charges)

    for i in range(number):
        for j in range(i+1, number):
            displacement = np.linalg.norm(chrage_positions[i] - charge_positions[j])

            if np.isclose(displacement, 0.0):
                raise ValueError("Two point charges cannot occupy the same position.")
            
            e = K_e * charges[i] * charges[j] / displacement

            energy += e

    return energy