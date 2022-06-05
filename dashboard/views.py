from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
@require_http_methods(["GET"])
def home(request):
    context = {}
    messages.info(request, 'You are loged in!')
    return render(request,'dashboard.html', context)