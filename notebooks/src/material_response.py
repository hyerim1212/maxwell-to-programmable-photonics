import numpy as np

epsilon_0 = 8.8541878128e-12
K_e = 1.0 / (4.0 * np.pi * epsilon_0)

def uniform_wire_response(voltage, length, radius, conductivity):

    if length <= 0 :
        raise ValueError("length must be positive.")

    if radius <= 0 :
        raise ValueError("radius must be positive.")

    if conductivity <= 0 :
        raise ValueError("conductivity must be positive.")    
    
    inner_electric_field = voltage / length
    
    current_density = conductivity * inner_electric_field
    
    area = np.pi * radius**2
    
    current = current_density * area
    
    resistance = length / (conductivity * area)

    power = voltage * current

    volumetric_power_density = conductivity * inner_electric_field **2

    joule_heating_power = conductivity * area * length * inner_electric_field **2 

    if joule_heating_power < 0 :
        raise ValueError("joule_heating_power must be nonnegative.")
        
    response = {
        "inner_electric_field": inner_electric_field,
        "current_density": current_density,
        "area": area,
        "current": current,
        "resistance": resistance,
        "power": power,
        "volumetric_power_density": volumetric_power_density,
        "joule_heating_power": joule_heating_power
    }

    return response
        
def dielectric_capacitor_fixed_charge(free_surface_charge_density, area, separation, relative_permittivity):
    """
    free_surface_charge_density: [C/m^2]
    area: [m^2]
    separation: [m]
    relative_permittivity: []
    """
    relative_permittivity = np.asarray(relative_permittivity, dtype=float)

    if np.any(relative_permittivity < 1):
        raise ValueError("All relative permittivity values must be at least 1.")
        
    if area <= 0 :
        raise ValueError("area must be positive.")

    if separation <= 0 :
        raise ValueError("separation must be positive.")

        
    absolute_permittivity = epsilon_0 * relative_permittivity

    susceptibility = relative_permittivity - 1

    free_charge = free_surface_charge_density * area

    D_field = free_surface_charge_density
    
    E_field = D_field / absolute_permittivity
    
    polarization = epsilon_0 * susceptibility * E_field
    
    bound_surface_charge_density_magnitude = abs(polarization)
    
    voltage_difference = E_field * separation
    
    capacitance = absolute_permittivity * area / separation
    
    energy_density = (1/2) * D_field * E_field
    
    stored_energy = (free_charge**2 )/ (2 * capacitance)

    response = {
        "absolute_permittivity": absolute_permittivity,
        "susceptibility": susceptibility,
        "free_charge": free_charge,
        "D_field": D_field,
        "E_field": E_field,
        "polarization": polarization,
        "bound_surface_charge_density_magnitude": bound_surface_charge_density_magnitude,
        "voltage_difference": voltage_difference,
        "capacitance": capacitance,
        "energy_density": energy_density,
        "stored_energy": stored_energy
    }
        
    return response
    
    
def layered_dielectric_capacitor(voltage, area, thicknesses: np.ndarray, relative_permittivities: np.ndarray):

    thicknesses = np.asarray(thicknesses, dtype=float)
    relative_permittivities = np.asarray( relative_permittivities, dtype=float,)

    if thicknesses.ndim != 1:
        raise ValueError("thicknesses dimension must be 1")

    if relative_permittivities.ndim != 1:
        raise ValueError("relative_permittivities must be one-dimensional.")

    if len(thicknesses) != len(relative_permittivities):
        raise ValueError

    if area <= 0 :
        raise ValueError("area must be positive.")

    if not np.all(thicknesses > 0) :
        raise ValueError("thicknesses must be positive.")
            

    if not np.all(relative_permittivities >= 1) :
        raise ValueError("relative_permittivity must be over 1.")

    absolute_permittivities = epsilon_0 * relative_permittivities

    electric_displacement = voltage / (np.sum(thicknesses / absolute_permittivities)) # scalar 

    electric_fields = electric_displacement / absolute_permittivities

    D_field = electric_fields * absolute_permittivities

    voltage_drops = electric_fields * thicknesses

    interface_positions = np.concatenate(([0.0], np.cumsum(thicknesses)))

    interface_potentials = voltage - np.concatenate(([0.0], np.cumsum(voltage_drops)))

    capacitance = area / (np.sum(thicknesses / absolute_permittivities))

    free_charge_from_capacitance = capacitance * voltage
    free_charge_from_displacement = electric_displacement * area

    if not np.isclose(free_charge_from_capacitance, free_charge_from_displacement, rtol=1e-10,
    atol=0.0):
        raise ValueError("Free charge calculated from capacitance and displacement do not agree.")


    polarizations = (epsilon_0 * (relative_permittivities - 1.0) * electric_fields)

    energy_densities = (0.5 * electric_fields * electric_displacement)

    layer_energies = (energy_densities * area * thicknesses)

    total_energy_from_layers = np.sum(layer_energies)

    response = {
        "absolute_permittivities": absolute_permittivities,
        "electric_displacement": electric_displacement,
        "electric_fields": electric_fields,
        "D_field": D_field,
        "voltage_drops": voltage_drops,
        "interface_positions": interface_positions,
        "interface_potentials": interface_potentials,
        "polarizations": polarizations,
        "capacitance": capacitance,
        "free_charge": free_charge_from_displacement,
        "energy_densities": energy_densities,
        "layer_energies": layer_energies,
        "total_energy": total_energy_from_layers,
    }

    return response


