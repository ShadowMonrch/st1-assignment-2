class AppointmentPersistence:
    def __init__(self):
        self.appointments = {}

    def find_by_id(self, appointment_id: str):
        return self.appointments.get(appointment_id)

    def save(self, appointment_id: str, appointment) -> None:
        self.appointments[appointment_id] = appointment