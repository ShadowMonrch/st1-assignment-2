from abc import ABC, abstractmethod


class AppointmentRepository(ABC):
    @abstractmethod
    def find_by_id(self, appointment_id: str):
        pass

    @abstractmethod
    def save(self, appointment_id: str, appointment):
        pass