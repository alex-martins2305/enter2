from django import forms
from .models import upload

class UploadFileForm(forms.ModelForm):
    class Meta:
        model= upload
        fields='__all__'
    
    def clean(self):
        return self.cleaned_data