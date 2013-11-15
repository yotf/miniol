from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Test(models.Model):
    att1 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.att1

class Student(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(
            verbose_name='email address',
            max_length=255
            )
    is_active = models.BooleanField(default=True)
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)

class Aktivnost(models.Model):
    ime = models.CharField(max_length=200,unique=True)
    is_active = models.BooleanField(default=True)

class Module(models.Model):
    title = models.CharField(max_length=200,unique=True)
    
    
class ZavrseneAktivnosti(models.Model):
    student = models.ForeignKey(Student)
    activities = models.ManyToManyField(Aktivnost,blank=True)


    
