from django.db import models
from Test2.models import Commint

class Post(models.Model):
    commit= models.CharField(max_length=50,unique=True)
    like = models.IntegerField(default=True)
    category = models.ForeignKey(Commint,on_delete= models.CASCADE,related_name='commints')

    def __str__(self):
        return self.commit