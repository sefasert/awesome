from django import forms

from .models import User

class DenemeForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

##########################################################

class NewUserForm(forms.ModelForm):
    
    class Meta():
        model = User
        fields = '__all__'
        

    

    
