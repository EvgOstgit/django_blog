from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm

# представление для отображения списка постов
def post_list(request):
    # запрашиваем у БД все записи таблицы Post (объекты класса Post)
    # Post - модель, которая описывает таблицу в БД
    # objects - это менеджер, который предоставляет методы для работы с записями в БД
    # .all() - это метод, который возвращает QuerySet (набор записей) со всеми объектами модели Post
    # ответный набор записей будет отсортирован в соответствии с правилом .order_by (-created_at - от новых записей к старым)
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    # формирование html-страницы на основе шаблона (шаблон находится в templates/blog/)
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})

# домашняя страница
def home(request):
    return render(request, 'blog/home.html')

# о нас
def about(request):
    return render(request, 'blog/about.html')

def posts_by_category(request, category_slug):
    # получаем категорию по slug
    # get_object_or_404 - функция Django, которая возвращает объект или вызывает ошибку 404, если он не найден
    category = get_object_or_404(Category, slug=category_slug)

    # фильтруем посты по категориям
    posts = Post.objects.filter(categories=category).order_by('-created_at')

    return render(request, 'blog/posts_by_category.html', {'category': category, 'posts': posts})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form, 'post': post})
    
def post_detail(request, pk, category_slug=None):
    post = get_object_or_404(Post, pk=pk)
    category = None
    if category_slug:
        try:
            category = Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            category = None
    return render(request, 'blog/post_detail.html', {'post': post, 'category': category})
