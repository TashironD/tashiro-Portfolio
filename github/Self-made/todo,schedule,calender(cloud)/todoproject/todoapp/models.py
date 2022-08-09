from django.db import models
from django.utils import timezone

# Create your models here.


class todolist(models.Model):

    title=models.CharField(max_length=20)
    memo=models.TextField(blank=True,null=True)
    type=models.IntegerField(choices=[(0,"ToDo"),(1,"Schedule")],default=0)
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField()
    done=models.BooleanField(default=False)#BooleanFieldは0、1の二択

    def __str__(self):
        return self.title