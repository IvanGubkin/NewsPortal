from django import forms
from .models import Post
from django.core.validators import ValidationError


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'text',
            'title',
            'category',
            'type_category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data
