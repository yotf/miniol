from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(
            verbose_name='email address',
            max_length=255
            )
    is_active = models.BooleanField(default=True)
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)
    def __unicode__(self):
        return self.user
        
class Module(models.Model):
    title = models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.title

class Aktivnost(models.Model):
    module = models.ForeignKey(Module)
    title = models.CharField(max_length=200,unique=True)
    is_active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.ime

    
class ZavrseneAktivnosti(models.Model):
    student = models.ForeignKey(Student)
    activities = models.ManyToManyField(Aktivnost,blank=True)


    
