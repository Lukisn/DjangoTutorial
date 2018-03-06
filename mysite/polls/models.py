from datetime import timedelta

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("publishing date")

    def __str__(self):
        return f"id={self.id}, text={self.question_text}"

    def was_published_recently(self):
        now = timezone.now()
        a_day_ago = now - timedelta(days=1)
        return a_day_ago <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"id={self.id}, text={self.choice_text}"
