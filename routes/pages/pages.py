from starlite import get, Template
from starlite.controller import Controller
from starlite.handlers import post
from starlite import Request, Redirect
from pydantic import ValidationError
from shared.urls import create_short_url, get_short_url
from schemas.urls import CreateURL


class BasicPageController(Controller):
    path = "/"

    @get(path="/not-found", name="404")
    async def homepage(self) -> Template:
        return Template(name="404.html")


class PageController(Controller):
    path = "/"

    @get(path="/", name="homepage")
    async def homepage(self) -> Template:
        return Template(name="pages/homepage.html")

    @get(path="/{uuid:str}", status_code=307)
    async def redirect_url(self, request: Request, uuid: str) -> Redirect:
        resp = await get_short_url(request, uuid)
        url = resp.dict().get("path")
        if url is None:
            url = request.app.route_reverse("404")
        return Redirect(path=url)

    @post(path="/short_url", name="short_url")
    async def short_url(
        self,
        request: Request,
    ) -> Template:
        data = await request.form()

        kwargs = {}
        for key, value in data.items():
            kwargs[key] = value
        try:
            kwargs = CreateURL(**kwargs).dict()
        except ValidationError as e:
            context = {"error": True, "fields": []}
            fields = []
            for error in e.errors():
                fields.append({"name": error.get("loc")[0], "msg": error.get("msg")})
            context["fields"] = fields
            return Template(name="pages/homepage.html", context=context)

        context = await create_short_url(request, **kwargs)
        return Template(name="pages/url.html", context=context.dict())
