import starlite

from app import events, routes


def create_app() -> starlite.Starlite:
    app = starlite.Starlite(
        route_handlers=[routes.router],
        on_startup=[events.create_redis_conn],
        on_shutdown=[events.destroy_redis_conn],
    )

    return app


app = create_app()
