from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

@login_required
@require_http_methods(["GET"])
def home(request):
    context = {}
    return render(request,'dashboard.html', context)

@login_required
@require_http_methods(["POST"])
def post_tweet(request):
    if request.is_ajax:
        print(request.POST)
    else:
        return JsonResponse({"error": "Not an ajax request"}, status=400)