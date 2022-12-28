from rise.response import Response
from rise.request import Request
from rise.app_helpers import AppHelpers

class ResponseFormatterMiddleware(AppHelpers):

    def process_response(self, req: Request, resp: Response):
        self._format_body_response(resp)
