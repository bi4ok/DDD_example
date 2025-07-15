from dataclasses import dataclass

@dataclass(frozen=True)
class Email:
    address: str

    def __post_init__(self):
        if "@" not in self.address:
            raise ValueError("Invalid email")
