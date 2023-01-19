from django.shortcuts import render
from posts.models import Post, Comment

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


def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post)

        context = {
            'post': post,
            'comments': comments
        }

        return render(request, 'posts/detail.html', context=context)
