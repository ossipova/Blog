from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class Comment (models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
