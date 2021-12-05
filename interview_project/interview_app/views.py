from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("physical port: Physical port 1 \n user1: user \n user2")