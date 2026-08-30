import numpy as np
import pytest

from src.verification import (
    absolute_error,
    relative_error,
    is_within_tolerance,
    phase_error,
    power_conservation_error,
)


def test_absolute_error_scalar():
    result = absolute_error(
        numerical_value=1.1,
        reference_value=1.0,
    )

    assert result == pytest.approx(0.1)


def test_absolute_error_array():
    numerical = np.array([1.0, 2.1, 2.9])
    reference = np.array([1.0, 2.0, 3.0])

    result = absolute_error(numerical, reference)

    expected = np.array([0.0, 0.1, 0.1])

    assert result == pytest.approx(expected)


def test_relative_error_scalar():
    result = relative_error(
        numerical_value=1.01,
        reference_value=1.0,
    )

    assert result == pytest.approx(0.01)


def test_relative_error_rejects_zero_reference():
    with pytest.raises(ValueError):
        relative_error(
            numerical_value=1.0,
            reference_value=0.0,
        )


def test_is_within_tolerance_accepts_close_value():
    result = is_within_tolerance(
        numerical_value=1.000001,
        reference_value=1.0,
        relative_tolerance=1e-5,
    )

    assert result is True


def test_is_within_tolerance_rejects_distant_value():
    result = is_within_tolerance(
        numerical_value=1.01,
        reference_value=1.0,
        relative_tolerance=1e-5,
    )

    assert result is False


def test_negative_tolerance_is_rejected():
    with pytest.raises(ValueError):
        is_within_tolerance(
            numerical_value=1.0,
            reference_value=1.0,
            relative_tolerance=-1e-5,
        )


def test_phase_error_handles_phase_wrapping():
    epsilon = 1e-6

    numerical = np.exp(1j * (np.pi - epsilon))
    reference = np.exp(1j * (-np.pi + epsilon))

    result = phase_error(numerical, reference)

    assert result == pytest.approx(2e-6)


def test_phase_error_rejects_zero_magnitude():
    with pytest.raises(ValueError):
        phase_error(
            numerical_value=0.0 + 0.0j,
            reference_value=1.0 + 0.0j,
        )


def test_power_conservation_error():
    result = power_conservation_error(
        reflectance=0.36,
        transmittance=0.64,
    )

    assert result == pytest.approx(0.0)