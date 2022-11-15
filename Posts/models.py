from django.db import models
from django.utils import timezone


class Post(models.Model):
    philospophy = ("philosophy", "Philosophy")
    mylife = ("MyLife", "mylife")
    Title = models.CharField(max_length=120)
    Content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    topics = models.CharField( max_length=30, choices= [philospophy, mylife], default="philosophy")

    def __str__(self) -> str:
        return self.Title
