from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("Hello World, You are at blog's index")
    
def detail(request, post_id):
    return HttpResponse(f"You are viewing post details page {post_id}")

def old_url_redirect(request):
    # return redirect("new_url") 
    # instead of hard coding this url we can use reverse from djano.urls
    return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
    return HttpResponse("This is the new URL")