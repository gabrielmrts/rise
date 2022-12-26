from rise import types
from rise.http_errors import HTTPNotFound
from rise.response import Response
import typing as t

class AppHelpers:

    def _build_common_headers(self, response: Response):
        headers = response.headers

        if not "Content-Length" in headers:
            headers.append((
                'Content-Length', response.get_content_length()
            ))