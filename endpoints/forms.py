from django import forms
from endpoints.models import Project


class ProForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'lang', 'code_challenge')


class ProjectForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Project name"
        })
    )
    lang = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Programming Language"
        })
    )
    code_challenge = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Here comes the code challenge!"
        })
    )


class ProjectEditForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Project name",
            "value": " {{ name }}"
        })
    )
    lang = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Programming Language"
        })
    )
    code_challenge = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Here comes the code challenge!"
        })
    )
    code_to_test = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Here comes your code!"
        })
    )


'''
class ProjectEditForm(forms.Form):
    name = forms.CharField()

    def project_edit(self):
        # send email using the self.cleaned_data dictionary
        pass
'''

class ProjectTestForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Project name",
            "value": "123"
        })
    )
    lang = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Programming Language"
        })
    )
    code_challenge = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Here comes the code challenge!"
        })
    )
    code_to_test = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Here comes your code!"
        })
    )
