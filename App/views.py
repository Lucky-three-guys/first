from math import ceil

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import Post


def post_list(request):
    page = int(request.GET.get('page',1))
    total = Post.objects.count()
    per_page = 10
    pages = ceil(total / per_page)
    start = (page-1) * per_page
    end = start + per_page
    posts = Post.objects.order_by('-id')[start:end]

    return render(request, 'post_list.html', context={
        "pages":range(pages),"posts":posts
    })

def create_post(request):
    if request.method == "POST":
        title = request.GET.get('title')
        content = request.GET.get('content')
        post = Post.objects.create(title=title,content=content)
        return redirect(reverse("app:post_list"))
    return render(request,'post_list.html')