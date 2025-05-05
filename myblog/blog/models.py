from django.db import models
from django.utils import timezone

# модель категории с единственным полем - названием
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# модель постов
class Post(models.Model):
    title = models.CharField(max_length=200) # заголовок поста
    content = models.TextField() # основной текст поста
    created_at = models.DateTimeField(default=timezone.now) # дата создания поста (по умолчанию - текущая)
    updated_at = models.DateTimeField(auto_now=True) # дата последнего обновления (по умолчанию автоматически обновляется при сохранении)
    categories = models.ManyToManyField(Category, related_name='posts') #related_name='posts' позволяет получить все посты, связанные с категорией

    def __str__(self):
        return self.title
    
# модель комментария
class Comment(models.Model):
    post_id = models.IntegerField()
    author = models.CharField(max_length=100)
    text =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"