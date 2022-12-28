from rise.response import Response
import json

class AppHelpers:

    def _build_common_headers(self, response: Response):
        headers = response.headers
        
        headers.append(('Content-Length', response.get_content_length()))
        headers.append(('Content-Type', response.get_content_type()))
    
    def _format_body_response(self, response: Response):
        content_type = response.get_content_type()

        if content_type == "application/json":
            response.body = json.dumps(response.body)

    def _process_middlewares(self, middlewares: list) -> list:
        middlewares_by_stage = {
            "before": [],
            "during": [],
            "after": [],
        }

        for middleware in middlewares:
            methods = {
                "process_request": "before",
                "process_resource": "during",
                "process_response": "after",
            }

            for method, stage in methods.items():
                if hasattr(middleware, method):
                    middlewares_by_stage[stage].append(getattr(middleware, method))

        return middlewares_by_stage