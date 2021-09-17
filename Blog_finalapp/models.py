from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)


class Blog_post(models.Model):
    Title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_on = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='pics')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_post')
    class Meta:
        db_table = 'Blog_post'
        ordering = ['-created_on']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})


class log(models.Model):
    email = models.CharField(max_length=50, unique=True)
    pwd = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'Logs'
# Create your models here.
