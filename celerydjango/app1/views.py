from app1.tasks import sleepy
from django.shortcuts import render
from django.http import HttpResponse
from app1.tasks import sleepy
# Create your views here.

def index(request):
    sleepy.delay(5)
    return HttpResponse("<h1>Done</h1>")
