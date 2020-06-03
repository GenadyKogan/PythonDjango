from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()
    image=models.ImageField(null=True, blank=True,upload_to="images/")
    objects = models.Manager()
    #news_articles=models.TextField(default='')
    def __str__(self):
        return self.title
    #def get_image(self,obj):
        #return mark_safe(f'<img scr={obj.images.url} width="50" hight="60"')
    def bit (self):
        if self.image:
            return u'<img src="%s" width="70"/>'% self.article_image.url
        else:
            return u'(none)'
    
    bit.allow_tags = True