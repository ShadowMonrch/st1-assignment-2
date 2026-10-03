class Practitioner:
    def __init__(
        self,
        identifier: str,
        name: str,
        specialty: str
    ) -> None:
        if not identifier:
            raise ValueError("Practitioner identifier cannot be empty")

        if not name:
            raise ValueError("Practitioner name cannot be empty")

        if not specialty:
            raise ValueError("Practitioner specialty cannot be empty")

        self.identifier = identifier
        self.name = name
        self.specialty = specialty

    def create(self) -> None:
        pass

    def view(self) -> str:
        return f"{self.name} - {self.specialty}"