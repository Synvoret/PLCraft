from django import forms

COLLECTION_CHOICES = [
    ("", "---"),
    ("bagpack", "Bagpack"),
    ("crochet", "Crochet"),
]


class CollectionForm(forms.Form):
    collection_type = forms.ChoiceField(
        choices=COLLECTION_CHOICES, widget=forms.Select(attrs={"class": "form-select"})
    )
