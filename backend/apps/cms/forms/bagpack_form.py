from django import forms

from apps.bagpack.models import Bagpack


class BagpackForm(forms.ModelForm):
    class Meta:
        model = Bagpack
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "season": forms.Select(attrs={"class": "form-select"}),
            "type": forms.Select(attrs={"class": "form-select"}),
        }
