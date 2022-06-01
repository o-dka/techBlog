from django.shortcuts import render
from django.utils import timezone
from .models import Post, Tag
from .forms import PostForm


def index(request):
    templates = 'blog/post_list.html'
    # title = "Последние обновления на сайте"
    posts = Post.objects.order_by('-published_date')[:]
    context = {
        'posts': posts,
    }
    return render(request, templates, context)


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    

# def post_list(request):
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {})

