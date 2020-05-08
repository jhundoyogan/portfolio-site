from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    tool_used = models.CharField(max_length=100, default='')
    app_link = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.summary
