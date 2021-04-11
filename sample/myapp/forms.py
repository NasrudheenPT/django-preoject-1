from django import forms
from django.forms import ModelForm
from .models import Student,img

class NewStudentForm(ModelForm):
    class Meta:
        model = Student
        fields="__all__"
        widgets={
            'name':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'age':forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
             'email':forms.EmailInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }

class ImageUploadForm(ModelForm):
    class Meta:
        model = img
        fields="__all__"

