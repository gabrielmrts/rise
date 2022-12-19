from rise.app import App    
from rise.response import Response
from rise.request import Request
import rise.http_errors as httperr
from rise import status

app = App()

def user(req: Request, resp: Response):
    
    resp.responseBody = req.context.PATH_INFO
    resp.responseHeaders = [
        ('Content-Type', 'text/plain')
    ]
    resp.responseStatusCode = status.HTTP_200_OK

def especific_user(req: Request, resp: Response, id, name):
    resp.responseBody = "id: {}, name: {}".format(id, name)
    resp.responseHeaders = [
        ('Content-Type', 'text/plain')
    ]
    resp.responseStatusCode = status.HTTP_200_OK

    return True

# app.add_route("/user", user)
app.add_route("/user/<id>/fog/<name>", especific_user)