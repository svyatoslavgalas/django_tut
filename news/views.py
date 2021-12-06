from django.shortcuts import render

from .models import Post


def news_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'news/list.html', ctx)


def news_detail(request, id):
    post = Post.objects.get(id=id)
    ctx = {
        'post': post,
    }
    return render(request, 'news/detail.html', ctx)
