# blog/models.py

# Django modules
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# MODEL:Post
class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)

	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
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