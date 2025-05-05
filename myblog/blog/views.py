from django.shortcuts import render
from .models import Post

# представление для отображения списка постов
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})