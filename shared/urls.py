from pydantic import AnyHttpUrl
from starlite import Request, HTTPException

import shortuuid
from schemas import urls, errors


async def create_short_url(
    request: Request, url: AnyHttpUrl, custom_path: str | None
) -> urls.UrlResponse | errors.FormFieldError:
    if url is None:
        return errors.FormFieldError(field="url", error="Missing Url")
    path = custom_path if custom_path else shortuuid.uuid(url)[:6]

    match = await request.cache.get(path)
    if match is None:
        await request.cache.set(path, url, 60)
    return urls.UrlResponse(path=path)


async def get_short_url(request: Request, uuid: str):
    match = await request.cache.get(uuid)
    if match is None:
        return HTTPException(status_code=404, detail="Url not found")
    return urls.UrlResponse(path=match)
