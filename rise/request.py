from rise import types

class Request:

    def __init__(self) -> None:
        self.context: types.RequestContext = types.RequestContext