from rise.app import App    
from rise.response import Response
from rise.request import Request
from rise.http_errors import HTTPNotFound
from rise import status

app = App()

def user(req: Request, resp: Response):
    
    resp.responseBody = req.context.RAW_URI
    resp.responseHeaders = [('Content-Type', 'text/plain')]
    resp.responseStatusCode = status.HTTP_200_OK

    return True

def especific_user(req: Request, resp: Response, id):
    resp.responseBody = id
    resp.responseHeaders = [
        ('Content-Type', 'text/plain')
    ]
    resp.responseStatusCode = status.HTTP_200_OK

    return True

def mid(req: Request, resp: Response):
    if req.context.REQUEST_METHOD == "GET":
        raise HTTPNotFound(description="request invalid")

app.add_middleware(mid)
app.add_route("/user", user)
app.add_route("/user/<id>", especific_user)