from pydantic import BaseModel, EmailStr

class CreateUserDTO(BaseModel):
    name: str
    email: EmailStr
