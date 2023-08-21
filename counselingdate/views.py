from django.shortcuts import render
from .models import CounselingDate
def display_counselingdate(request):

    data = CounselingDate.objects.all() #for all the records 
    context={
       
      'data':data,
    
    } 

    return render(request, 'counseling.html', context)