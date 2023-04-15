from pydantic import BaseModel, AnyHttpUrl


class UrlResponse(BaseModel):
    path: str | None


class CreateURL(BaseModel):
    url: AnyHttpUrl
    custom_path: str | None
