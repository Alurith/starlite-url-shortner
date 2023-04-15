from starlite import Router

from .controllers import urls

from .pages import pages

api_router = Router(
    path="/api",
    route_handlers=[urls.UrlController],
)


page_router = Router(
    path="/",
    route_handlers=[pages.PageController, pages.BasicPageController],
)

root_router = [api_router, page_router]
