from django.db import models

# Create your models here.


class Question(models.Model):
    ques = models.CharField(max_length=200)
    cat = models.CharField(max_length=20)

    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    ans4 = models.CharField(max_length=100)

    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.ques
