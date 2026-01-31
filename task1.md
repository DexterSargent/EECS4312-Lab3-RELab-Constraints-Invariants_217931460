1. Should the patient_id follow a specific alphanumeric format or is it just an internal integer?
2. Should the medication field store the generic chemical name, the brand name, or a standardized drug identification number?
3. How should the system handle quantity for different units of measurement, for example if a medication is liquid (mL) versus pills (units).
4. Is there a minimum age requirement for patients receiving specific classes of medications?
5. What is the protocol for emergency dispensing if the patient’s ID cannot be immediately verified?
6. Should the system track the specific batch or lot number for each DispenseEvent in case of a recall?
7. Is there a global maximum allowable dose for any medication, or is this limit specific to each individual drug type?
8. Should the system prevent dispensing if the expiration date of the current stock is in the past?
