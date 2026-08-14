import numpy as np

def snell_angle(refractive_index_incident: float, refractive_index_transmitted: float, incident_angle: float | np.ndarray) -> float | np.ndarray:

    incident_angle = np.asarray(incident_angle, dtype=float)
    
    transmitted_sin = (refractive_index_incident / refractive_index_transmitted * np.sin(incident_angle))

    if np.any(transmitted_sin > 1.0):
        raise ValueError("No real transmitted angle exists under total internal reflection.")

    transmitted_angle = np.arcsin(transmitted_sin)

    return transmitted_angle
        
    

def fresnel_coefficients(refractive_index_incident: float, refractive_index_transmitted: float, incident_angle: float | np.ndarray, polarization: str):

    incident_angle = np.asarray(incident_angle, dtype=float)
    
    transmitted_angle = snell_angle(refractive_index_incident, refractive_index_transmitted, incident_angle)

    if polarization in ("s", "TE") :
        
        r_s = ((refractive_index_incident * np.cos(incident_angle)) - (refractive_index_transmitted * np.cos(transmitted_angle))) / ((refractive_index_incident * np.cos(incident_angle)) + (refractive_index_transmitted * np.cos(transmitted_angle)))

        t_s = 2 * refractive_index_incident * np.cos(incident_angle) / ((refractive_index_incident * np.cos(incident_angle)) + (refractive_index_transmitted * np.cos(transmitted_angle)))

        response = {
            "r_s": r_s,
            "t_s": t_s
        }

        return response

    elif polarization in ("p", "TM") : 
        
        r_p = ((refractive_index_transmitted * np.cos(incident_angle)) - (refractive_index_incident * np.cos(transmitted_angle))) / ((refractive_index_transmitted * np.cos(incident_angle)) + (refractive_index_incident * np.cos(transmitted_angle)))

        t_p = 2 * refractive_index_incident * np.cos(incident_angle) / ((refractive_index_transmitted * np.cos(incident_angle)) + (refractive_index_incident * np.cos(transmitted_angle)))

        response = {
            "r_p": r_p,
            "t_p": t_p
        }

        return response

    else :
        raise ValueError("enter the right polarization.")
        



def reflectance(reflection_coefficient: float | np.ndarray) -> float | np.ndarray:

    R = np.abs(reflection_coefficient) ** 2

    return R



def transmittance(transmission_coefficient, refractive_index_incident: float, refractive_index_transmitted: float, incident_angle: float | np.ndarray, transmitted_angle: float | np.ndarray) -> float | np.ndarray:

    incident_angle = np.asarray(incident_angle, dtype=float)
    transmitted_angle = np.asarray(transmitted_angle, dtype=float)

    T = (refractive_index_transmitted * np.cos(transmitted_angle))/(refractive_index_incident * np.cos(incident_angle)) * np.abs(transmission_coefficient) **2

    return T



def critical_angle(refractive_index_incident: float, refractive_index_transmitted: float) -> float:

    if not refractive_index_incident > refractive_index_transmitted :
        raise ValueError("It doesn't have a critical angle")

    critical_angle = np.arcsin(refractive_index_transmitted / refractive_index_incident)

    return critical_angle



def evanescent_decay_constant(wavelength_vacuum: float | np.ndarray, refractive_index_incident: float, refractive_index_transmitted: float, incident_angle: float | np.ndarray) -> float | np.ndarray:

    wavelength_vacuum = np.asarray(wavelength_vacuum, dtype=float)
    incident_angle = np.asarray(incident_angle, dtype=float)

    if np.any(wavelength_vacuum) <= 0:
        raise ValueError("wave length in a vacuum must be positive.")

    if np.any(refractive_index_incident * np.sin(incident_angle) <= refractive_index_transmitted):
        raise ValueError("It does not need to regard evanescent decay constant")
    
    decay_constant = (2 * np.pi * refractive_index_transmitted / wavelength_vacuum) * ((refractive_index_incident / refractive_index_transmitted)**2 * np.sin(incident_angle)**2 - 1 ) ** (1/2)

    return decay_constant

    