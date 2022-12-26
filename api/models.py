from django.db import models

# Create your models here.


class Registration(models.Model):
    id = models.AutoField(primary_key = True)
    Name = models.CharField(blank=True, max_length=500, null=True)
    Phone = models.CharField(blank=True, max_length=500, null=True,unique=True)
    Email = models.CharField(blank=True, max_length=500, null=True, unique=True)
    Gender = models.CharField(blank=True, max_length=500, null=True)
    Password = models.CharField(blank=True, max_length=500, null=True)

class FAQ(models.Model):
    Idd = models.CharField(blank=True, max_length=500, null=True)
    qs1 = models.CharField(blank=True, max_length=500, null=True)
    qs2 = models.CharField(blank=True, max_length=500, null=True)
    qs3 = models.CharField(blank=True, max_length=500, null=True)
    qs4 = models.CharField(blank=True, max_length=500, null=True)
    qs5 = models.CharField(blank=True, max_length=500, null=True)



    ans1 = models.CharField(blank=True, max_length=500, null=True)
    ans2 = models.CharField(blank=True, max_length=500, null=True)
    ans3 = models.CharField(blank=True, max_length=500, null=True)
    ans4 = models.CharField(blank=True, max_length=500, null=True)
    ans5 = models.CharField(blank=True, max_length=500, null=True)

