from django import forms
from django.forms import RadioSelect

from .models import Review


class FormReview(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'rating', 'review')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-name',
                    'id': 'name',
                    'aria-describedby': 'nameHelp',
                    'placeholder': 'Логин',
                }
            ),

            'rating': RadioSelect(
                attrs={
                    'id': 'rating',
                },
                choices=[
                    (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
                ]
            ),
            'review': forms.Textarea(
                attrs={
                    'class': 'form-text',
                    'id': 'content',
                    'placeholder': 'Комментарий',
                }
            ),
        }
