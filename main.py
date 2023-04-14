from starlite import Starlite, CacheConfig, TemplateConfig
from starlite.cache.redis_cache_backend import (
    RedisCacheBackendConfig,
    RedisCacheBackend,
)
from starlite.contrib.jinja import JinjaTemplateEngine

from routes import routes

config = RedisCacheBackendConfig(url="redis://redis", port=6379, db=0)
redis_backend = RedisCacheBackend(config=config)

cache_config = CacheConfig(backend=redis_backend)

app = Starlite(
    route_handlers=routes.root_router,
    cache_config=cache_config,
    template_config=TemplateConfig(directory="templates", engine=JinjaTemplateEngine),
)
