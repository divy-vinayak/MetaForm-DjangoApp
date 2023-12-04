from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class QuestionType(models.Model):
    question_type = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.question_type

class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.question_text

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    submitter_info = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.response