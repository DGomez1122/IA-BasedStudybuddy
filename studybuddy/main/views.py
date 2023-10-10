from django.shortcuts import render

# Create your views here.
# main/views.py

def index(request):
    return render(request, 'main/index.html')
