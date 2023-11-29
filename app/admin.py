from django.contrib import admin
from app import models

# Register your models here.

admin.site.register(models.Answer)
admin.site.register(models.Form)
admin.site.register(models.Question)

class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = [
        'question_type'
    ]

admin.site.register(models.QuestionType, QuestionTypeAdmin)
admin.site.register(models.Response)