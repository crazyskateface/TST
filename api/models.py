from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey('auth.User', related_name='questions')
    
    
    
    def __unicode__(self):
        return self.question_text
    