class UserExist:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            print('User is authenticated')
        else:
            print('User is not authenticated')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
