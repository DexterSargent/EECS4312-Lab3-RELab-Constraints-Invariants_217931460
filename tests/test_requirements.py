# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases

import pytest
from src.dispense import DispenseEvent, invariant_holds

def test_positive_dose_constraint():
    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="Advil", dose_mg=0, quantity=1)
    
    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="Advil", dose_mg=-10, quantity=1)

def test_maximum_dosage_limit_constraint():
    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="Advil", dose_mg=1500, quantity=1)

def test_duplicate_dispensing_invariant():
    event1 = DispenseEvent(patient_id="P1", medication="Advil", dose_mg=200, quantity=1)
    event2 = DispenseEvent(patient_id="P1", medication="Advil", dose_mg=200, quantity=1)
    
    existing_events = [event1]
    
    assert invariant_holds(existing_events, event2) is False
