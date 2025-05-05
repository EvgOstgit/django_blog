from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# модель категории с единственным полем - названием
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        print(f"Saving category: {self.name}")
        if not self.slug:
            self.slug = slugify(self.name)
            print(f"Generated slug: {self.slug}")
        super().save(*args, **kwargs)

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
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Комментарий от {self.author}'