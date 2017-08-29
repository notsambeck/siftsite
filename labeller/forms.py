from django import forms
from .models import Image, Choice


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('filename', 'correct_label', 'source',)


class ImageChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice',)
