from pydantic import AnyHttpUrl
from starlite.controller import Controller
from starlite.handlers import post, get
from starlite import Request
from schemas import urls
from shared.urls import create_short_url, get_short_url


class UrlController(Controller):
    path = "/v1"

    @post(path="/")
    async def create_url(
        self, request: Request, url: AnyHttpUrl, custom_path: str | None
    ) -> urls.UrlResponse:
        return await create_short_url(request, url, custom_path)

    @get(path="/{uuid:str}")
    async def get_url(self, request: Request, uuid: str) -> urls.UrlResponse:
        resp = await get_short_url(request, uuid)
        return resp
