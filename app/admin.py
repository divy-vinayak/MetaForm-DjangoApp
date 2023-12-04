from django.contrib import admin
from app import models

# Register your models here.

admin.site.register(models.Answer)

class FormAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'title',
        'description',
        'created_at',
        'updated_at'
    ]
admin.site.register(models.Form, FormAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'form',
        'question_text',
        'question_type',
        'order',
        'created_at',
        'updated_at'
    ]
admin.site.register(models.Question, QuestionAdmin)

class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = [
        'question_type'
    ]
admin.site.register(models.QuestionType, QuestionTypeAdmin)
admin.site.register(models.Response)