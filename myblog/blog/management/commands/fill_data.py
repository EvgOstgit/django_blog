from django.core.management.base import BaseCommand
from blog.models import Category, Post, Comment
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Заполняет базу данных постами и комментариями для существующих категорий'

    def handle(self, *args, **kwargs):
        # Получаем все категории
        categories = Category.objects.all()

        # Проверяем, есть ли категории
        if not categories:
            self.stdout.write(self.style.ERROR('Нет категорий в базе данных!'))
            return

        # Добавляем по два поста для каждой категории
        for category in categories:
            for i in range(2):  # по два поста для каждой категории
                post = Post.objects.create(
                    title=f'Пост {i + 1} в категории {category.name}',
                    content=f'Содержимое поста {i + 1} в категории {category.name}. Тут будет информация о посте.',
                    created_at=timezone.now(),
                    updated_at=timezone.now()
                )
                # Добавляем пост в категорию
                post.categories.add(category)  # Связываем пост с категорией
                self.stdout.write(self.style.SUCCESS(f'Создан пост: {post.title}'))

                # Добавляем комментарии к каждому посту
                for j in range(2):  # по два комментария для каждого поста
                    comment = Comment.objects.create(
                        post=post,
                        author=f'Автор {j + 1} комментария к посту "{post.title}"',
                        text=f'Комментарий {j + 1} к посту "{post.title}"',
                        created_date=timezone.now()
                    )
                    self.stdout.write(self.style.SUCCESS(f'Создан комментарий: {comment.text}'))

        self.stdout.write(self.style.SUCCESS('Заполнение базы данных завершено!'))
