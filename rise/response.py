import typing as t

class Response:

    def __init__(self) -> None:
        self.responseBody = {}
        self.responseStatusCode = '200 OK'
        self.responseHeaders: t.List[t.Tuple] = [('Content-Type', 'text/plain')]

    def get_content_length(self) -> str:
        return str(len(str(self.responseBody)))