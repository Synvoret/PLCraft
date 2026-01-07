from django import forms

from apps.crochet.models import Crochet


class CrochetForm(forms.ModelForm):
    class Meta:
        model = Crochet
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "type": forms.Select(attrs={"class": "form-select"}),
        }
