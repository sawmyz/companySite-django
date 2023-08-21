from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CounselingForm
from.models import CounselingDate


def index(request):

    # data = CounselingDate.objects.all() #for all the records 
    # context={
       
    #   'data':data,
    
    # } 
    # return render(request, 'counseling.html', context)
#    if request.method == "POST":
        form = CounselingForm(request.POST)
        if form.is_valid():
            print("Form Is Valid")
            form.save()
        else:
            print("Form Not is valid")
            print(form.errors)

        return render(request, "counseling.html", {"form": form} )

#    else:
        # form = CounselingForm()

#    return render(request, "counseling.html", {"form": form})

# def counseling_add(request):
#     # if this is a POST request we need to process the form data

#     data = CounselingDate.objects.all() #for all the records 
#     context={   
#       'data':data,
#     } 
#     if request.method == "POST":
#         form = CounselingForm(request.POST)
#         if form.is_valid():
#             print("Form Is Valid")
#             form.save()
#         else:
#             print("Form Not is valid")
#             print(form.errors)

#         return render(request, "counseling.html", {"form": form} )

#     else:
#         form = CounselingForm()

#     return render(request, "counseling.html", {"form": form})