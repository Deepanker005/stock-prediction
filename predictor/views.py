from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    # Instead of HttpResponse, we now "render" the HTML template
    return render(request, 'index.html')