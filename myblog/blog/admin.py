from django.contrib import admin
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug') # отображение slug в списке
    prepopulated_fields = {'slug': ('name',)} # Автоматическое заполнение slug

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)