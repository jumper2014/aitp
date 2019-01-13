from django.db import models

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # max_length 参数。这个参数的用处不止于用来定义数据库结构，
    # 也用于验证数据，我们稍后将会看到这方面的内容。
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text