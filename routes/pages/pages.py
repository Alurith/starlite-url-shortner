from starlite import get, Template
from starlite.controller import Controller
from starlite.handlers import post
from starlite import Request, Redirect

from shared.urls import create_short_url, get_short_url
from schemas.urls import CreateURL
from lib.forms import Form


class CreateURLForm(Form):
    form_model = CreateURL
    include = ["__all__"]
    method = "POST"

    def validate_custom_path(self):
        ...


class BasicPageController(Controller):
    path = "/"

    @get(path="/not-found", name="404")
    async def not_found(self) -> Template:
        return Template(name="404.html")


class PageController(Controller):
    path = "/"

    @get(path="/", name="homepage")
    async def homepage(self) -> Template:
        form = CreateURLForm()
        context = {"form": form}
        return Template(name="pages/homepage.html", context=context)

    @post(path="/", name="short_url", status_code=302)
    async def short_url(
        self,
        request: Request,
    ) -> Template:
        context = {}
        data = await request.form()

        kwargs = {}
        for key, value in data.items():
            kwargs[key] = value

        form = CreateURLForm(initials=kwargs)
        if form.is_valid:
            urlresponse = await create_short_url(request, **kwargs)
            context = urlresponse.dict()

        context["form"] = form
        return Template(name="pages/homepage.html", context=context)

    @get(path="/{uuid:str}", status_code=302)
    async def redirect_url(self, request: Request, uuid: str) -> Redirect:
        resp = await get_short_url(request, uuid)
        url = resp.dict().get("path")
        if url is None:
            url = request.app.route_reverse("404")
        return Redirect(path=url)
