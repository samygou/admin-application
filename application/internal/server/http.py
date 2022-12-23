from application.interface import RouterHandle, IBackend, new_router_handler


def new_http_server(backend: IBackend) -> RouterHandle:
    return new_router_handler(backend)
