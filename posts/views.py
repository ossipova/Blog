from django.shortcuts import render
from posts.models import Post

# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context = {
            'posts': posts,
            'message': 'It is message from view'
        }

        return render(request, 'posts/posts.html', context=context)

