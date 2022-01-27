# blog/models.py

# Django modules
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# MODEL: Author
class Author(models.Model):
	author_name = models.ForeignKey(User, on_delete=models.CASCADE)
	author_slug = models.SlugField(max_length=250)
	author_thumbnail = models.ImageField(blank=True,null=True,upload_to='uploads/authors/%Y/%m/%d')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created',)
		verbose_name_plural = "Authors"

	# def __str__(self):
	# 	return self.author_name  

# MODEL:Post
class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)

	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
	content = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	image = models.ImageField(blank=True,null=True,upload_to='uploads/posts/%Y/%m/%d')

	class Meta:
		ordering = ('-publish',)
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title  