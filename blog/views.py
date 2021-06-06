from django.shortcuts import render
from django.conf.urls import include

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# Create your views here.
