from django import forms
from .models import Labratory_test

class testForm(forms.ModelForm):
    class Meta:
        model= Labratory_test
        fields=['test_name','test_Price']