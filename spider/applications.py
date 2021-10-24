import typing
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import BaseRoute

class Spider(Starlette):
    def __init__(self, debug: bool = False, routes: typing.Sequence[BaseRoute] = None, middleware: typing.Sequence[Middleware] = None, exception_handlers: typing.Dict[typing.Union[int, typing.Type[Exception]], typing.Callable] = None, on_startup: typing.Sequence[typing.Callable] = None, on_shutdown: typing.Sequence[typing.Callable] = None, lifespan: typing.Callable[["Starlette"], typing.AsyncContextManager] = None) -> None:
        pass
    