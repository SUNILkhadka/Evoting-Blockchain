from django import forms
from dashboard.models import Candidate
from django.contrib.auth.models import User

class AddCandidate(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ("name", "team", "slogan", "description")
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'team':forms.TextInput(attrs={'class':'form-control'}),
            'slogan':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'})
        }

class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email")
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
           }