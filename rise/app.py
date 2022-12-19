import typing as t
from rise.response import Response
from rise.request import Request
from rise import status
from rise.http_errors import HTTPError
from rise.constants import *
from rise import types

class App():
    
    _routes = {}
    _start_response: callable = None
    _context: types.RequestContext = types.RequestContext
    
    def __call__(self, env: t.Dict, start_response: t.Callable) -> t.Iterable:
        self._load_context(env)

        response = Response()
        request = Request()

        self._start_response = start_response

        try:
            route = self._handle_route(request, response)

            if not route:
                return EMPTY_BODY
        except HTTPError as e:
            start_response(e.status, e.responseHeaders)
            return e.description

        self._build_common_headers(response)
        
        start_response(response.responseStatusCode, response.responseHeaders)

        return [str(response.responseBody).encode()]

    def _build_common_headers(self, response: Response):
        headers = response.responseHeaders

        if not "Content-Length" in headers:
            headers.append((
                'Content-Length', response.get_content_length()
            ))

    def _load_context(self, env: dict): 
        requestContext = types.RequestContext
        requestHeaders = types.HTTPHeaders

        for key in env:
            if key.startswith("HTTP_"):
                setattr(requestHeaders, key, env[key])
            else:
                setattr(requestContext, key, env[key])

        requestContext.HTTP_HEADERS = requestHeaders

        self._context = requestContext

    def _handle_route(self, req, res):
        routes = self._routes
        path = self._context.PATH_INFO

        for route, handler in routes.items():
            route_segments = route.split('/')
            path_segments = path.split('/')

            if len(route_segments) != len(path_segments):
                continue

            route_params = {}

            for route_segment, path_segment in zip(route_segments, path_segments):
                if route_segment.startswith('<') and route_segment.endswith('>'):
                    param_name = route_segment[1:-1]
                    route_params[param_name] = path_segment
                elif route_segment != path_segment:
                    break
            else:
                return handler(req, res, **route_params)

        self._start_response(status.HTTP_404_NOT_FOUND, [('Content-Type', 'text/plain')])
        return None

    def add_route(self, path: t.AnyStr, resource: t.Callable) -> None: 
        self._routes[path] = resource