import json


class CorsAllowOriginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = "*"

        return response

class ContentTypeJsonHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        is_response_json = True

        try:
            json.loads(response.content)
        except ValueError:
            is_response_json = False

        if is_response_json:
            response['Content-Type'] = "application/json"

        return response
