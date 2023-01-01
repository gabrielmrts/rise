from rise.app import App    
from rise.response import Response
from rise.request import Request
from rise import status

app = App()

class ResourceCollection:

    def post(self, req: Request, resp: Response):
        resp.body = req.context.body_json["hello"]
        resp.status = status.HTTP_201_CREATED

    def get(self, req: Request, resp: Response):
        resp.body = {"email": req.context.account_email}

class ResourceWithRouteParams:

    def get(self, req: Request, resp: Response, id):
        resp.body = f"User ID: {id}"

class AuthenticationMiddleware():
    """
    Middleware to authenticate user
    """
    def process_resource(self, req: Request, resp: Response):
        req.context.account_email = "user@email.com"


app.add_middleware(AuthenticationMiddleware())
app.add_route("/user", ResourceCollection())
app.add_route("/user/<id>", ResourceWithRouteParams())