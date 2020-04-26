from django import forms

#from .models import Book


class PDFForm(forms.ModelForm):
    class Meta:
        fields = ('variable', 'year', 'pdf')