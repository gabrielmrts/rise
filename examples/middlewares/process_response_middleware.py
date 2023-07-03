from rise.app import App    
from rise.response import Response
from rise.request import Request

app = App()

class ProcessResponseMiddleware():
    """
    This middleware can be useful for process the request response.
    This type of middleware runs after the process resource.
    """
    def process_response(self, req: Request, resp: Response):
        if req.context.http_content_type == "application/json":
            req.context.body_json["app_version"] = "1"
            
app.add_middleware(ProcessResponseMiddleware())