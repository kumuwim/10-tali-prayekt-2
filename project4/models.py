from django.db import models


# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    sur_name=models.CharField(blank=False,max_length=100,null=False)
    created_at=models.TimeField(auto_now_add=True)
    sur_name=models.CharField(max_length=100,blank=False,null=False)
    age=models.PositiveIntegerField(default=0,blank=False)



    def __str__(self):
        return self.name   
    