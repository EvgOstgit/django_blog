from django.shortcuts import render
from .models import Post

# представление для отображения списка постов
def post_list(request):
    # запрашиваем у БД все записи таблицы Post (объекты класса Post)
    # Post - модель, которая описывает таблицу в БД
    # objects - это менеджер, который предоставляет методы для работы с записями в БД
    # .all() - это метод, который возвращает QuerySet (набор записей) со всеми объектами модели Post
    # ответный набор записей будет отсортирован в соответствии с правилом .order_by (-created_at - от новых записей к старым)
    posts = Post.objects.all().order_by('-created_at')

    # формирование html-страницы на основе шаблона (шаблон находится в templates/blog/)
    return render(request, 'blog/post_list.html', {'posts': posts})

# домашняя страница
def home(request):
    return render(request, 'blog/home.html')

# о нас
def about(request):
    return render(request, 'blog/about.html')