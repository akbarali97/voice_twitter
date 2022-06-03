from django.shortcuts import render, redirect

# Create your views here.
def home(self):
    return redirect('sso_login')

def login(request):
    return render(template_name="<h1>hello</h1>")