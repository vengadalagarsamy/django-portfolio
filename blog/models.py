from django.db import models

#model for each post
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='portfolio/images/')
    description = models.TextField()

#alter how admin portal looks
def __str__(self):
    return self.title
