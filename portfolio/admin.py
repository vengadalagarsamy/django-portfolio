from django.contrib import admin
from .models import Project

#project objects accessed through admin portal
admin.site.register(Project)
