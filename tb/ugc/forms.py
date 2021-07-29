from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'external_id',
            'name',
            'firstname',

        )
        widgets = {
            'name': forms.TextInput,
            'firstname': forms.TextInput,
        }