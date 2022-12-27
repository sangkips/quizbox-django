from django.db import models
from authuser.models import User

# Create your models here.

Votes = (
    ("up", "up"),
    ("down", "down"),
)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):

    question_id = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.question_id)


class Vote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_choice = models.CharField(max_length=10, choices=Votes, default=None)
    quetion_id = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer_id = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vote_choice
