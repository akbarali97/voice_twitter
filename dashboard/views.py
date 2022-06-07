from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Tweet, Comment
from django.core.exceptions import ObjectDoesNotExist
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
        return JsonResponse({"success": 'tweet posted'}, status=200)
    else:
        return JsonResponse({"error": "audio-file not found"}, status=404)

@login_required
@require_http_methods(["POST"])
def post_comment(request):
    if request.FILES.get('audio-file', False) and request.POST.get('tweet_id', False):
        try:
            tweet = Tweet.objects.get(id=request.POST['tweet_id'])
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Tweet does not exist"}, status=404)
        uploaded_file = request.FILES['audio-file']
        Comment.objects.create(
            user=request.user,
            tweet=tweet,
            comment=uploaded_file
        )
        return JsonResponse({"success": 'comment posted'}, status=200)
    else:
        return JsonResponse({"error": "Bad request. Check request body."}, status=400)