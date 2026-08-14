import numpy as np

def snell_angle(refractive_index_incident: float, refractive_index_transmitted: float, incident_angle: float) -> float:
    
    transmitted_sin = (refractive_index_incident / refractive_index_transmitted) * np.sin(incident_angle) 

    if transmitted_sin > 1.0:
        raise ValueError("No real transmitted angle exists under total internal reflection.")

    transmitted_angle = np.arcsin(transmitted_sin)

    return transmitted_angle
        
    

def fresnel_coefficients(refractive_index_incident: float, refractive_index_transmitted: float, incident_angle: float, polarization: str):

    tolerance = 1e-6
    
    transmitted_sin = (refractive_index_incident / refractive_index_transmitted) * np.sin(incident_angle) 

    if transmitted_sin > 1 :
        raise ValueError("No real transmitted angle exists under total internal reflection.")

    transmitted_angle = np.arcsin(transmitted_sin)

    if polarization in ("s", "TE") :
        
        r_bot = ((refractive_index_incident * np.cos(incident_angle)) - (refractive_index_transmitted * np.cos(transmitted_angle))) / ((refractive_index_incident * np.cos(incident_angle)) + (refractive_index_transmitted * np.cos(transmitted_angle)))

        t_bot = 2 * refractive_index_incident * np.cos(incident_angle) / ((refractive_index_incident * np.cos(incident_angle)) + (refractive_index_transmitted * np.cos(transmitted_angle)))

        response = {
            "r_bot": r_bot,
            "t_bot": t_bot
        }

        return response

    elif polarization in ("p", "TM") : 
        
        r_parallel = ((refractive_index_transmitted * np.cos(incident_angle)) - (refractive_index_incident * np.cos(transmitted_angle))) / ((refractive_index_transmitted * np.cos(incident_angle)) + (refractive_index_incident * np.cos(transmitted_angle)))

        t_parallel = 2 * refractive_index_incident * np.cos(incident_angle) / ((refractive_index_transmitted * np.cos(incident_angle)) + (refractive_index_incident * np.cos(transmitted_angle)))

        response = {
            "r_parallel": r_parallel,
            "t_parallel": t_parallel
        }

        return response

    else :
        raise ValueError("enter the right polarization.")
        



def reflectance(reflection_coefficient) -> float:

    R = np.abs(reflection_coefficient) ** 2

    return R



def transmittance(transmission_coefficient, refractive_index_incident: float, refractive_index_transmitted: float, incident_angle: float, transmitted_angle: float) -> float:

    T = (refractive_index_transmitted * np.cos(transmitted_angle))/(refractive_index_incident * np.cos(incident_angle)) * np.abs(transmission_coefficient) **2

    return T



def critical_angle(refractive_index_incident: float, refractive_index_transmitted: float) -> float:

    if not refractive_index_incident > refractive_index_transmitted :
        raise ValueError("It doesn't have a critical angle")

    critical_angle = np.arcsin(refractive_index_transmitted / refractive_index_incident)

    return critical_angle



def evanescent_decay_constant(wavelength_vacuum: float, refractive_index_incident: float, refractive_index_transmitted: float, incident_angle: float) -> float:

    if wavelength_vacuum <= 0:
        raise ValueError("wave length in a vacuum must be positive.")

    if refractive_index_incident * np.sin(incident_angle) <= refractive_index_transmitted:
        raise ValueError("It does not need to regard evanescent decay constant")
    
    dcay_constant = (2 * np.pi * refractive_index_transmitted / wavelength_vacuum) * ((refractive_index_incident / refractive_index_transmitted)**2 * np.sin(incident_angle)**2 - 1 ) ** (1/2)

    return dcay_constant

    