from django.contrib.auth import logout

def logout_view(request):
    logout(request)