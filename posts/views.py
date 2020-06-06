from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect


def posts_list(request):
    posts = Post.objects.all()
    data = {'posts': posts}
    return render(request, 'post/list.html', context=data)


def post_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if post:
        data = {'post': post}
        return render(request, 'post/view.html', context=data)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
