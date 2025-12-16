from pydantic import BaseModel


class ErrorSchema(BaseModel):
    statusCode: int
    message: str
