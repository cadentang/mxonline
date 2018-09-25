__author__ = 'caden'
__data__ = ' 23:33'
from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)
