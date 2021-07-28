from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'user_id',
            'username',
            'firstname',
            'lastname'
        )
        widgets = {
            'username': forms.TextInput,
            'firstname': forms.TextInput,
            'lastname': forms.TextInput
        }