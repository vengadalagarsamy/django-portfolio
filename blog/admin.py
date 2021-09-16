from django.contrib import admin
from .models import Blogpost

#show blogposts in admin portal
admin.site.register(Blogpost)
