import typing as t
from rise.response import Response
from rise.request import Request
from rise.app_helpers import AppHelpers
from rise import types
from rise.http_errors import HTTPError, HTTPNotFound
import inspect

class App(AppHelpers):
    
    # Application Routes
    _routes = {}
    
    # Method to return the http response
    _start_response: callable = None

    # Context of application
    # Allow pass variables through the request session
    _context: types.RequestContext = types.RequestContext

    # Methods that are called before process all resources
    _middlewares: t.List[callable] = []

    # Methods allowed by this framework
    _http_methods = (
        "get", 
        "post",
        "patch",
        "put",
        "delete"
    )
    
    def __call__(self, env: t.Dict, start_response: t.Callable) -> t.Iterable:
        """WSGI `app` method.
        Makes instances of App callable from a WSGI server. May be used to
        host an App or called directly in order to simulate requests when
        testing the App.
        (See also: PEP 3333)
        Args:
            env (dict): A WSGI environment dictionary
            start_response (callable): A WSGI helper function for setting
                status and headers on a response.
        """

        self._load_context(env)
        self._start_response = start_response

        response = Response()
        request = Request(self._context)
        
        try:
            for middleware in self._middlewares:
                middleware(request, response)
            self._handle_route(request, response)
        except HTTPError as e:
            start_response(e.status, e.headers)
            return e.description

        self._build_common_headers(response)
        
        start_response(response.status, response.headers)

        return [str(response.body).encode()]

    def _load_context(self, env: dict): 
        request_context = types.RequestContext
        request_headers = types.HTTPHeaders

        for key in env:
            if key.startswith("HTTP_"):
                setattr(request_headers, key, env[key])
            else:
                setattr(request_context, key, env[key])

        request_context.HTTP_HEADERS = request_headers

        self._context = request_context

    def _handle_route(self, req, res):
        routes = self._routes
        path = self._context.PATH_INFO
        method = req.context.REQUEST_METHOD.lower()

        for route, methods in routes.items():
            route_segments = route.split('/')
            path_segments = path.split('/')

            if len(route_segments) != len(path_segments):
                continue

            handler = methods.get(method)

            if handler is None:
                continue

            route_params = {}

            for route_segment, path_segment in zip(route_segments, path_segments):
                if route_segment.startswith('<') and route_segment.endswith('>'):
                    param_name = route_segment[1:-1]
                    route_params[param_name] = path_segment
                elif route_segment != path_segment:
                    break
            else:
                # Check how many args a resource have
                resource_args = [arg for arg in inspect.getfullargspec(handler).args]

                for param in list(route_params):
                    if param not in resource_args:
                        route_params.pop(param, None)

                return handler(req, res, **route_params)

        raise HTTPNotFound("Route not found")

    def add_route(self, path: t.AnyStr, resource: object) -> None: 
        self._routes[path] = {}

        for method in self._http_methods:
            if method in dir(resource):
                route = {
                    method: resource.__getattribute__(method)
                }
                self._routes[path].update(route)
        
    def add_middleware(self, resource) -> None:
        self._middlewares.append(resource)