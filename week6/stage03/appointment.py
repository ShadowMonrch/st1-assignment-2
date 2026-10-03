from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"


class AppointmentStateError(Exception):
    pass


class Appointment:
    def __init__(
        self,
        patient,
        practitioner,
        appointmentTime: datetime,
        status: AppointmentStatus = AppointmentStatus.SCHEDULED
    ) -> None:
        self.patient = patient
        self.practitioner = practitioner
        self.appointmentTime = appointmentTime
        self.status = status

    def create(self) -> None:
        pass

    def change(self, new_time: datetime) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise AppointmentStateError(
                "Cannot change a cancelled appointment."
            )

        self.appointmentTime = new_time

    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise AppointmentStateError(
                "Appointment has already been cancelled."
            )

        self.status = AppointmentStatus.CANCELLED