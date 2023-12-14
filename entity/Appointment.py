class Appointment:
    def __init__(self, patient_id, doctor_id, appointment_date, description):
        # The appointment_id is not included here since it's auto-incremented in the database
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.description = description

    # ... other methods and properties

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}, " \
               f"Date: {self.appointment_date}, Description: {self.description}"
