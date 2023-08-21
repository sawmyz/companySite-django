from django.db import models
from counselingdate.models import CounselingDate,CounselingTime


class Counseling(models.Model):
    counseling_time = models.ForeignKey(CounselingTime, on_delete=models.CASCADE,default=1,related_name='counseling_session')
    counseling = models.ForeignKey(CounselingDate, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)


    def __str__(self):
        return self.name