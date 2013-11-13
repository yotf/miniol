from django.db import models

# Create your models here.

class Test(models.Model):
    att1 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.att1

    
