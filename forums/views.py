from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'forums/post_list.html', {'posts': posts})


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'forums/detail.html',{'post':post})