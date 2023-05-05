from django.contrib import admin
from .models import NewsAndEvents, Session, Semester

# Register your models here.

admin.site.register(NewsAndEvents)
admin.site.register(Semester)
admin.site.register(Session)