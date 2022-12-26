import typing as t

class Response:

    def __init__(self) -> None:
        self.body = {}
        self.status = '200 OK'
        self.headers: t.List[t.Tuple] = [('Content-Type', 'text/plain')]

    def get_content_length(self) -> str:
        body_size = len(str(self.body))

        return str(body_size)