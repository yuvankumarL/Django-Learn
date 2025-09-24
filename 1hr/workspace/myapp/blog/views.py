from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

# posts = [
#     {'id': 1, 'title': 'Post 1', 'content': 'Content for Post 1'},
#     {'id': 2, 'title': 'Post 2', 'content': 'Content for Post 2'},
#     {'id': 3, 'title': 'Post 3', 'content': 'Content for Post 3'},
#     {'id': 4, 'title': 'Post 4', 'content': 'Content for Post 4'},
# ]

def index(request):
    # return HttpResponse("Hello World, You are at blog's index")
    blog_title = "Latest Post"
    all_posts = Post.objects.all()

    #paginate
    paginator = Paginator(all_posts, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'blog_title': blog_title, 'page_obj': page_obj})
    
def detail(request, slug):
    # return HttpResponse(f"You are viewing post details page {post_id}")
    # static data
    # post = next((item for item in posts if item['id'] == int(post_id)), None)

    # getting data from model by post id
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does not Exists!ss")

    logger = logging.getLogger("TESTING")
    logger.debug(f'post variable is {post}')
    return render(request, 'blog/detail.html', {'post': post, 'related_posts':related_posts})

def old_url_redirect(request):
    # return redirect("new_url") 
    # instead of hard coding this url we can use reverse from djano.urls
    return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
    return HttpResponse("This is the new URL")