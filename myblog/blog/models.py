from django.db import models
from django.utils import timezone

# модель постов
class Post(models.Model):
    title = models.CharField(max_length=200) # заголовок поста
    content = models.TextField() # основной текст поста
    created_at = models.DateTimeField(default=timezone.now) # дата создания поста (по умолчанию - текущая)
    updated_at = models.DateTimeField(auto_now=True) # дата последнего обновления (по умолчанию автоматически обновляется при сохранении)

    def __str__(self):
        return self.title