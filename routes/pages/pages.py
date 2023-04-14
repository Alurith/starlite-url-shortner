from starlite import get, Template
from starlite.controller import Controller
from starlite.handlers import post
from starlite import Request, Redirect

from shared.urls import create_short_url, get_short_url
from schemas.urls import CreateURL


class PageController(Controller):
    path = "/"

    @get(path="/")
    async def homepage(self) -> Template:
        return Template(name="pages/homepage.html")

    @get(path="/{uuid:str}", status_code=307)
    async def redirect_url(self, request: Request, uuid: str) -> Redirect:
        resp = await get_short_url(request, uuid)
        return Redirect(**resp.dict())

    @post(path="/short_url", name="short_url")
    async def short_url(
        self,
        request: Request,
    ) -> Template:
        data = await request.form()

        kwargs = {}
        for key, value in data.items():
            kwargs[key] = value

        context = await create_short_url(request, **CreateURL(**kwargs).dict())
        return Template(name="pages/url.html", context=context.dict())
