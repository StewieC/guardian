from django.contrib import admin
from .models import Incident, Article

admin.site.register(Incident)
admin.site.register(Article)