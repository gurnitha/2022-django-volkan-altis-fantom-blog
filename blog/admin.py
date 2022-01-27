# blog/admin.py

# Django modules
from django.contrib import admin

# Locals
from . models import Post, Author 

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('author_name', 'author_thumbnail')
	list_filter = ('author_name',)
	search_fields = ('author_name',)
	prepopulated_fields = {'author_slug': ('author_name',)}
	raw_id_fields = ('author_name',)
	date_hierarchy = 'created'
