from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=180)
    summary = models.CharField(max_length=250 , blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/' , blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail' , args=[str(self.id)])