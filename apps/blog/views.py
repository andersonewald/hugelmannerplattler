from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    posts = Post.objects.all().order_by("-data_publicacao")
    return render(request, "blog/lista_posts.html", {"posts": posts})

def detalhe_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/detalhe_post.html", {"post": post})