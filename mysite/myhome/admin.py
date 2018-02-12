from django.contrib import admin
from .models import intent, answers, questions

admin.site.register(intent)
admin.site.register(answers)
admin.site.register(questions)

# Register your models here.
