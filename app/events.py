import redis
import starlite
from starlite.cache import redis_cache_backend

from app import config

REDIS_URL = config.settings.redis_url
REDIS_PORT = config.settings.redis_port


def create_redis_conn(state: starlite.State):
    config = redis_cache_backend.RedisCacheBackendConfig(
        url=REDIS_URL,
        port=REDIS_PORT,
        db=0,
    )
    redis_backend = redis_cache_backend.RedisCacheBackend(config=config)
    state.redis = redis_backend._redis_int  # type: ignore[assignment]
    starlite.CacheConfig(backend=redis_backend)


def destroy_redis_conn(state: starlite.State):
    if isinstance(state.redis, redis.Redis):
        state.redis.close()
