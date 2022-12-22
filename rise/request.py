from rise import types

class Request:

    def __init__(self, context: types.RequestContext) -> None:
        self.context = context