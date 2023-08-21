from django.db import models


class CounselingDate(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name
    
class CounselingTime(models.Model) :

    counseling = models.ForeignKey(CounselingDate, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)    

    def __str__(self):
        return self.time