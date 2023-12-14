class PatientNumberNotFoundException(Exception):
    def __init__(self, patient_number):
        super().__init__(f"Patient with number {patient_number} not found.")
        self.patient_number = patient_number
