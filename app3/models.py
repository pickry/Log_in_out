from django.db import models

# Create your models here.
class quizmodel(models.Model):
    question = models.TextField(max_length=200)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)

    def __str__(self):
        return self.question
    

class Students(models.Model):
    name = models.CharField(max_length=100)
    wrong = models.IntegerField()
    score = models.IntegerField()
    right = models.IntegerField()


