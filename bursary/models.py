from django.db import models
from django.contrib.auth.models import User

class university(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255,null=True,default="Name your university here")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.Name}")

class cdfofficial(models.Model):
    uSer = models.ForeignKey(university, on_delete=models.CASCADE, null=True,)


class institution(models.Model):
    school = models.ForeignKey(university, on_delete=models.CASCADE,default=0)
    phone = models.CharField(max_length=10, null=True, )
    student = models.CharField(max_length=255, null=True, )
    datecreated = models.DateTimeField(auto_now_add=True,null=True)
    Cheque = models.ImageField(null=True, blank=False)


    def __str__(self):
        return f"{self.student}"