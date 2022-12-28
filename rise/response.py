import typing as t
from rise import status

class Response:

    def __init__(self) -> None:
        self.body = {}
        self.status = status.HTTP_200_OK
        self.headers: t.List[t.Tuple] = []

    def get_content_length(self) -> str:
        """
        Get the body size
        """
        
        body_size = len(str(self.body))

        return str(body_size)
    
    def get_content_type(self) -> str:
        """
        Get the body response content type
        """

        if isinstance(self.body, dict):
            return "application/json"
        else:
            return "text/plain"