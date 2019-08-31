from django.contrib import admin

# Register your models here.

# register Question: these objects will should have an admin interface
# python3.7 manage.py runserver >  http://127.0.0.1:8000/admin/polls/question/
from .models import Question

admin.site.register(Question)