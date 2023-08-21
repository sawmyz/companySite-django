from django.contrib import admin
from .models import CounselingDate
from .models import CounselingTime

admin.site.register(CounselingDate)
admin.site.register(CounselingTime)