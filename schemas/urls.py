from pydantic import BaseModel


class UrlResponse(BaseModel):
    path: str | None


class CreateURL(BaseModel):
    url: str
    custom_path: str | None
