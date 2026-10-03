class Patient:
    def __init__(self, name: str) -> None:
        if not name:
            raise ValueError("Patient name cannot be empty")

        self.name = name

    def create(self) -> None:
        pass

    def update(self, name: str) -> None:
        if not name:
            raise ValueError("Patient name cannot be empty")

        self.name = name

    def view(self) -> str:
        return self.name