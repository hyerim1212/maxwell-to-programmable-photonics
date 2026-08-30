import numpy as np
import pytest

from src.optics import (
    snell_angle,
    fresnel_coefficients,
    reflectance,
    transmittance,
    complex_field,
    superpose_fields,
    field_intensity,
)


def test_snell_angle_at_normal_incidence():
    transmitted_angle = snell_angle(
        refractive_index_incident=1.5,
        refractive_index_transmitted=1.0,
        incident_angle=0.0,
    )

    assert transmitted_angle == pytest.approx(0.0)


def test_equal_indices_produce_no_reflection():
    coefficients = fresnel_coefficients(
        refractive_index_incident=1.5,
        refractive_index_transmitted=1.5,
        incident_angle=0.0,
        polarization="TE",
    )

    result = reflectance(coefficients["r_s"])

    assert result == pytest.approx(0.0)


@pytest.mark.parametrize("polarization", ["TE", "TM"])
def test_fresnel_power_conservation(polarization):
    n_incident = 1.5
    n_transmitted = 1.0
    incident_angle = np.radians(20.0)

    transmitted_angle = snell_angle(
        n_incident,
        n_transmitted,
        incident_angle,
    )

    coefficients = fresnel_coefficients(
        n_incident,
        n_transmitted,
        incident_angle,
        polarization,
    )

    if polarization == "TE":
        reflection_coefficient = coefficients["r_s"]
        transmission_coefficient = coefficients["t_s"]
    else:
        reflection_coefficient = coefficients["r_p"]
        transmission_coefficient = coefficients["t_p"]

    R = reflectance(reflection_coefficient)

    T = transmittance(
        transmission_coefficient,
        n_incident,
        n_transmitted,
        incident_angle,
        transmitted_angle,
    )

    assert R + T == pytest.approx(1.0, abs=1e-12)


def test_equal_amplitude_constructive_interference():
    field_1 = complex_field(amplitude=1.0, phase=0.0)
    field_2 = complex_field(amplitude=1.0, phase=0.0)

    total_field = superpose_fields(field_1, field_2)
    intensity = field_intensity(total_field)

    assert intensity == pytest.approx(4.0)


def test_equal_amplitude_destructive_interference():
    field_1 = complex_field(amplitude=1.0, phase=0.0)
    field_2 = complex_field(amplitude=1.0, phase=np.pi)

    total_field = superpose_fields(field_1, field_2)
    intensity = field_intensity(total_field)

    assert intensity == pytest.approx(0.0, abs=1e-14)