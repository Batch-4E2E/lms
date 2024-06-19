from django.contrib.auth import logout

class logout_when_refresh:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if request method is GET and not from a login or logout URL
        if request.method == 'GET' and not request.path.startswith('/login/') and not request.path.startswith('/logout/'):
            logout(request)
        return response