from allauth.account.forms import SignupForm
from django import forms
from django.forms import ModelForm

from src.accounts.models import User


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'profile_image', 'first_name', 'last_name', 'phone_number', 'cnic'
        ]


class MyCustomSignupForm(SignupForm):
    cnic = forms.CharField(help_text="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'CNIC'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cnic'].label = 'CNIC'

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.cnic = request.POST.get('cnic')
        user.save()
        return user
