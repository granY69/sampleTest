from django.db import models

# Create your models here.

class Questions(models.Model):
    q_text = models.CharField(max_length=200)
    p_date = models.DateTimeField('date published')
    def __str__(self):
        return self.q_text
    class Meta:
        db_table = "quest_table"


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    class Meta:
        db_table = "choice_table"