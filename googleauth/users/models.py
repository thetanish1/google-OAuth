from django.db import models

# Create your models here.
class BlogModel(models.Model):
    username = models.CharField(max_length=15)
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username + ' ' + self.title
    
    class Meta:
        ordering = ['-pub_date']
