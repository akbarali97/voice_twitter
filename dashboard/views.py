from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Tweet

@login_required
@require_http_methods(["GET"])
def home(request):
    context = {'tweets': Tweet.objects.all()}
    return render(request,'dashboard.html', context)

@login_required
@require_http_methods(["POST"])
def post_tweet(request):
    if request.FILES.get('audio-file', False):
        uploaded_file = request.FILES['audio-file']
        Tweet.objects.create(
            user=request.user,
            tweet=uploaded_file
        )
        return JsonResponse({"success": 'audio-file.mp3'}, status=200)
    else:
        return JsonResponse({"error": "base64audio not found"}, status=400)