import typing as t
from rise import status

class HTTPError(Exception):
    def __init__(self, http_status: int, description: t.Optional[str] = None, *args: object) -> None:
        super().__init__(*args)
        
        self.status = http_status
        self.description = [str(description).encode()]
        self.headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(str(description))))]

class HTTPNotFound(Exception):

    def __init__(self, description: t.Optional[str] = None, *args: object) -> None:
        super().__init__(*args)
        
        raise HTTPError(status.HTTP_404_NOT_FOUND, description)