class AppointmentService:
    def __init__(self, repository):
        self.repository = repository

    def find_appointment(self, appointment_id: str):
        return self.repository.find_by_id(appointment_id)

    def save_appointment(self, appointment) -> None:
        self.repository.save(appointment)