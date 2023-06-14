from .models import Mentor
from django import forms

class volunter_form(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['Name','Mobileno','Email','Profession']
        widgets = {'Name':forms.TextInput(attrs = {'class':'form-control space'}),
                'Mobileno':forms.TextInput(attrs = {'class':'form-control space'}),
                'Email':forms.EmailInput(attrs = {'class':'form-control space'}),
                'Profession':forms.TextInput(attrs = {'class':'form-control space'}),
                }