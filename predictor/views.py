from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! The stock predictor API is awake.")