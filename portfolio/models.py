from django.db import models

#model for each project added to the site
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    backend = models.CharField(max_length=250)
    frontend = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

def __str__(self):
    return self.title
