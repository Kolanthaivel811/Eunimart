from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth import get_user_model
from .models import *

class NewUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'mobile', 'userName')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'signupForm',
                'placeholder': _('Name')}),
            'email': forms.EmailInput(attrs={
                'class': 'signupForm',
                'placeholder': _('Email')}),
            'mobile': forms.TextInput(attrs={
                'class': 'signupForm',
                'placeholder': _('Mobile')}),
            'userName': forms.TextInput(attrs={
                'class': 'signupForm',
                'placeholder': _('UserName')})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

