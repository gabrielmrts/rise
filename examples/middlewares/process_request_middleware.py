from rise.app import App    
from rise.response import Response
from rise.request import Request

app = App()

class ProcessRequestMiddleware():
    """
    This middleware process the request before process the resource.
    Good for verify the http method and otherelse like content type.
    """
    def process_request(self, req: Request, resp: Response):
        if req.context.http_content_type == "application/json":
            ...
        if req.context.request_method == "POST":
            ...

app.add_middleware(ProcessRequestMiddleware())