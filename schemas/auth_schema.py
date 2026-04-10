from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenFCMRequest(BaseModel):
    user_id: int
    fcm_token: str
