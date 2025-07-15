from uuid import UUID, uuid4

class UserDM:
    def __init__(self, uuid: str, name: str, email: 'Email'):
        self.uuid = uuid
        self.name = name
        self.email = email

