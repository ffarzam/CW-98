class AuthenticationDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        if self.is_authenticated(request):
            return self.func(request, *args, **kwargs)
        else:
            raise ValueError("login first")

    @staticmethod
    def is_authenticated(request):
        return request.get("header").get("token") == "sometoken"


@AuthenticationDecorator
def api_endpoint(request):
    print("doing somthing")


request = {"header": {"token": "sometoken"}}


api_endpoint(request)
