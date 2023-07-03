from rise.app import App    
from rise.response import Response
from rise.request import Request

app = App()

class ProcessResourceMiddleware():
    """
    This middleware type is used for pre resource processing.
    For example, fetching user data based on user token
    and putting it on the request context for futher access.
    """
    def process_resource(self, req: Request, resp: Response):
        user_data = {"username": "john"}
        req.context["user_data"] = user_data

class ExampleResource():
    """
    Example resource for using the above middleware
    """

    def get(self, req: Request, resp: Response):
        user_data = req.context["user_data"]

app.add_route("/user", ExampleResource())
app.add_middleware(ProcessResourceMiddleware())