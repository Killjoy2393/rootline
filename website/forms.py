from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'class': 'form-control',}),
            'phone': forms.TextInput(attrs={'class': 'form-control',}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
