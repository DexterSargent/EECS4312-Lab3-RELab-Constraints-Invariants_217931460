
class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """

        # 1. The dose must be a positive value
        if dose_mg <= 0:
            raise ValueError("Dose must be a positive value.")
        
        # 2. The quantity dispensed must be a positive integer
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity dispensed must be a positive integer.")
            
        # 3. Each medication has a maximum daily dose [cite: 96]
        # (Using a 1000mg threshold as a standard system constraint for this lab) [cite: 101]
        MAX_DAILY_DOSE = 1000 
        if dose_mg > MAX_DAILY_DOSE:
            raise ValueError(f"Dose exceeds the maximum daily limit of {MAX_DAILY_DOSE}mg.")

        # 5. All doses are expressed in milligrams.
        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        pass
