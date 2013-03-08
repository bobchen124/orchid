from django.db import models

# Create your models here.

class Course(models.Model):
    roomId = models.CharField(max_length=64, unique=True)
    courseName = models.CharField(max_length=100)
    #orgid = models.CharField(max_length=60)
    #userstate = models.IntegerField()
    createTime = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = u'course'
