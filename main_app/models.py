from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

<<<<<<< HEAD
# Create your models here.
#article test

=======
>>>>>>> e5af42f7b8433240dd0e01e6b1d6890339b012dd
class Article(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField(max_length=3000)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('articles_detail', kwargs={'article_id': self.id})

    class Meta:
        ordering = ['-date']

class Profile(models.Model):
<<<<<<< HEAD
    bio = models.CharField(max_length=200)
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> e5af42f7b8433240dd0e01e6b1d6890339b012dd
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField(max_length=100)
    articles = models.ManyToManyField(Article)


    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'profile_id': self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for profile_id: {self.profile_id} @{self.url}"

