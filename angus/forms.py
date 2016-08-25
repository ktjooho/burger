#-*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from angus.models import UserProfile, GuestBook
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.password_validation import MinimumLengthValidator,password_validators_help_texts
from django.core.exceptions import ValidationError

class GuestBookForm(forms.ModelForm):

    #content = forms.TextInput(label='Contents')

    #author = forms.CharField(label='Author',widget=forms.TextInput(),initial=)
    #
    #content = forms.CharField(label="Contents", widget=forms.Textarea(), help_text='Put Down any msg',
    #                          initial='Tetst',disabled=True)
    #def __init__(self):
        #self.

    #ip_address = forms.GenericIPAddressField

    class Meta:
        model = GuestBook
        fields = ('author','content',)



class UserForm(forms.ModelForm):
    #validator = MV(min_length=6)
    password = forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')
    def checkValidPassword(self):
        try:
            validate_password(self.data['password'])
        except ValidationError as e:
            self.add_error('password',e)
            return False
        return True

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                           widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(label="ImageField")
    class Meta:
        model = UserProfile
        fields=('picture',)


class LoginForm(AuthenticationForm):
    #def confirm_login_allowed(self, user):

    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

