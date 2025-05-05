from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# представление для отображения списка постов
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# домашняя страница
def home(request):
    return HttpResponse("""
        <h1>Главная страница</h1>
        <ul>
            <li><a href="/about/">О нас</a></li>
            <li><a href="/articles/">Статьи</a></li>
        </ul>
    """)

# о нас
def about(requests):
    return HttpResponse("""
        <h1>О нас</h1>
        <p>Это простой блог на Django.</p>
        <a href="/">На главную</a>
""")