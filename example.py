from rise.app import App    
from rise.response import Response
from rise.request import Request
from rise.http_errors import HTTPNotFound
from rise import status

app = App()

class ResourceCollection:

    def post(self, req: Request, resp: Response):
        resp.body = "using a post method"
        resp.headers = [('Content-Type', 'text/plain')]
        resp.status = status.HTTP_200_OK

    def get(self, req: Request, resp: Response):
        resp.body = "using a get method"
        resp.headers = [('Content-Type', 'text/plain')]
        resp.status = status.HTTP_200_OK

class ResourceWithRouteParams:

    def get(self, req: Request, resp: Response, id):
        resp.body = f"ID: {id}"
        resp.headers = [('Content-Type', 'text/plain')]
        resp.status = status.HTTP_200_OK

def mid(req: Request, resp: Response):
    if req.context.REQUEST_METHOD == "GET":
        raise HTTPNotFound(description="request invalid")

#app.add_middleware(mid)
app.add_route("/user", ResourceCollection())
app.add_route("/user/<id>", ResourceWithRouteParams())