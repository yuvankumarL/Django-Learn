from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    # return HttpResponse("Hello World, You are at blog's index")
    blog_title = "Latest Post"
    posts = [
        {'title': 'Post 1', 'content': 'Content for Post 1'},
        {'title': 'Post 2', 'content': 'Content for Post 2'},
        {'title': 'Post 3', 'content': 'Content for Post 3'},
        {'title': 'Post 4', 'content': 'Content for Post 4'},
    ]
    return render(request, 'blog/index.html', {'blog_title': blog_title, 'posts': posts})
    
def detail(request, post_id):
    # return HttpResponse(f"You are viewing post details page {post_id}")
    return render(request, 'blog/detail.html')

def old_url_redirect(request):
    # return redirect("new_url") 
    # instead of hard coding this url we can use reverse from djano.urls
    return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
    return HttpResponse("This is the new URL")