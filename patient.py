class Patient:
    def __init__(self, name, date_of_birth, contact_number):
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact_number = contact_number
        self.medical_records = []
        self.appointments = []

    def add_medical_record(self, medical_record):
        self.medical_records.append(medical_record)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)


class MedicalRecord:
    def __init__(self, record_id, record_date, diagnosis, medication):
        self.record_id = record_id
        self.record_date = record_date
        self.diagnosis = diagnosis
        self.medication = medication


class Appointment:
    def __init__(self, appointment_id, appointment_date, doctor_name, purpose):
        self.appointment_id = appointment_id
        self.appointment_date = appointment_date
        self.doctor_name = doctor_name
        self.purpose = purpose


class PatientPortal:
    def __init__(self):
        self.patients = []

    def register_patient(self, patient):
        self.patients.append(patient)

    def login(self):
        # Placeholder login functionality
        print("Logged in successfully!")
        return True

    def display_medical_records(self, patient):
        for record in patient.medical_records:
            print(f"Record ID: {record.record_id}")
            print(f"Record Date: {record.record_date}")
            print(f"Diagnosis: {record.diagnosis}")
            print(f"Medication: {record.medication}")
            print("")

    def display_appointments(self, patient):
        for appointment in patient.appointments:
            print(f"Appointment ID: {appointment.appointment_id}")
            print(f"Appointment Date: {appointment.appointment_date}")
            print(f"Doctor: {appointment.doctor_name}")
            print(f"Purpose: {appointment.purpose}")
            print("")

    def run(self):
        logged_in = self.login()
        if logged_in:
            print("Welcome to the Patient Portal!")
            patient_name = input("Enter your name: ")
            contact_number = input("Enter your contact number: ")
            patient = Patient(patient_name, None, contact_number)
            self.register_patient(patient)

            while True:
                print("\n--- Menu ---")
                print("1. View Medical Records")
                print("2. View Appointments")
                print("3. Exit")

                choice = input("Enter your choice (1-3): ")
                if choice == "1":
                    self.display_medical_records(patient)
                elif choice == "2":
                    self.display_appointments(patient)
                elif choice == "3":
                    print("Thank you for using the Patient Portal. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")


# Usage Example:
portal = PatientPortal()
portal.run()
