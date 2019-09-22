from django import forms
from .models import Contact
class FormContact(forms.ModelForm):
    name = forms.CharField(label="Ho ten", max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Contact
        fields = ['name','phone','email', 'message']