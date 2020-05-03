from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField(default='')
    date = models.DateTimeField()
    objects = models.Manager()
    #news_articles=models.TextField(default='')
    def __str__(self):
        return self.title