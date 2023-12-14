from DAO.IHospitalService import IHospitalService
from util.DBConnUtil import DBConnUtil
from Exception.PatientNumberNotFoundException import  PatientNumberNotFoundException

class HospitalServiceImpl(IHospitalService):
    def execute_query(self, query, values=None):
        connection = None
        cursor = None
        try:
            connection = DBConnUtil.open_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, values)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:

            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def execute_update(self, query, values=None):
        connection = None
        cursor = None
        try:
            connection = DBConnUtil.open_connection()
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error executing update: {e}")
            return False
        finally:

            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_appointment_by_id(self, appointment_id):
        query = "SELECT * FROM appointments WHERE appointmentId = %s"
        result = self.execute_query(query, (appointment_id,))
        return result[0] if result else None

    def get_appointments_for_patient(self, patient_id):
        query = "SELECT * FROM appointments WHERE patient_id = %s"
        return self.execute_query(query, (patient_id,))


    '''
    def update_appointment(self, date, new_description, appointment_id):
        query = "UPDATE appointments SET appointment_date = %s, description = %s WHERE appointmentId = %s"
        values = (date, new_description, appointment_id)
        return self.execute_update(query, values)
    '''

    def update_appointment(self, date, new_description, appointment_id):
        query = "UPDATE appointments SET appointment_date = %s, description = %s WHERE appointmentId = %s"
        values = (date, new_description, appointment_id)

        connection = None
        cursor = None

        try:
            connection = DBConnUtil.open_connection()
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()

            if cursor.rowcount == 0:
                raise PatientNumberNotFoundException(f"Appointment with ID {appointment_id} not found.")

            print("Appointment updated successfully.")
            return True

        except PatientNumberNotFoundException as e:
            print(f"Error: {e}")
            return False

        except Exception as e:
            print(f"Error updating appointment: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def cancel_appointment(self, appointment_id):
        query = "DELETE FROM appointments WHERE appointmentId = %s"
        connection = None
        cursor = None

        try:
            connection = DBConnUtil.open_connection()
            cursor = connection.cursor()
            cursor.execute(query, (appointment_id,))
            rows_affected = cursor.rowcount  # Get the number of affected rows

            if rows_affected == 0:
                raise PatientNumberNotFoundException(f"Appointment with ID {appointment_id} not found.")
            else:
                print("Appointment canceled successfully.")

        except PatientNumberNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error cancelling appointment: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_appointments_for_doctor(self, doctor_id):
        query = "SELECT * FROM appointments WHERE doctor_id = %s"
        return self.execute_query(query, (doctor_id,))

    def schedule_appointment(self, appointment):
        query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, description) VALUES (%s, %s, %s, %s)"
        values = (appointment.patient_id, appointment.doctor_id, appointment.appointment_date, appointment.description)
        return self.execute_update(query, values)

    def Show_All(self):
        query="SELECT * FROM appointments "
        result = self.execute_query(query)
        return result

