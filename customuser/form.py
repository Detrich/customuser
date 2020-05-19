from django import forms

class LoginUser(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupUser(forms.Form):
    username = forms.CharField(max_length=50)
    display_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)