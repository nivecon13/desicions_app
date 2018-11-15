from django.db import models
from django.utils import timezone


class Decision(models.Model):
    username = models.CharField(max_length=30, default='Anonymous')
    question = models.CharField(max_length=255, default='Unknown')
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    decision_made = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "Option 1 :" + self.option_1 + " Option 2 :" + self.option_2 + "Decision :" + str(self.decision)