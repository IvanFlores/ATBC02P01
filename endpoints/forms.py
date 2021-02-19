from django import forms


class ProjectForm(forms.Form):
    lang = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Programming Language"
        })
    )
    code = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Here comes your code!"
        })
    )

