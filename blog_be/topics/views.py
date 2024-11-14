from django.shortcuts import render
from django.http import HttpResponse
from .models import Story


def index(request):
    story_title = Story.objects
    
    return HttpResponse("Hello, world. You're at the topical index. edfadfs")