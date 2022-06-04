from django.shortcuts import redirect

# Create your views here.
def home(self):
    return redirect('/sso/accounts/login')