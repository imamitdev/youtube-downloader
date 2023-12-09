from django.shortcuts import render
from pytube import YouTube

# Create your views here.


def youtube(request):
    if request.method == "POST":
        url = request.POST["url"]
        my_video = YouTube(url)
        video = my_video.streams.get_highest_resolution()
        video.download()
    return render(request, "index.html")
