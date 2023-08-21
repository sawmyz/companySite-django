# from django import forms
# from counseling.models import Counseling

# class CounselingForm(forms.Form):
#     class Meta : model = Counseling


#     name = forms.CharField(label="name", max_length=100)
#     lastname = forms.CharField(label="lastname", max_length=100)
#     phone = forms.CharField(label="phone", max_length=100)
#     subject = forms.CharField(label="subject", max_length=100)
from django import forms
from .models import Counseling

class CounselingForm(forms.ModelForm):
    class Meta:
        model = Counseling
        fields = ['name', 'lastname','phone','subject','counseling','counseling_time']