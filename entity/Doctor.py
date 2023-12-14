class Doctor:
    def __init__(self, doctor_id, first_name, last_name, specialization, contact_number):
        self.doctor_id = doctor_id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.contact_number = contact_number

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.first_name} {self.last_name}, " \
               f"Specialization: {self.specialization}, Contact: {self.contact_number}"
