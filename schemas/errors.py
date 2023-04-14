from pydantic import BaseModel


class NotFoundError(BaseModel):
    detail: str | None


class FormFieldError(BaseModel):
    field: str
    error: str
