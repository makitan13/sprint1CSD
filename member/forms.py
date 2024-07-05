from django.forms import ModelForm
from django import forms
from .models import Member

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.TextInput(attrs={'class':"form-control"}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
   
