from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User
from django import forms
class RegistrationForm(UserCreationForm):
	

	class Meta:
		model = User
		fields = ('email', 'username', 'password1', 'password2','contactno', 'address', 'gender' )

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			User = User.objects.exclude(pk=self.instance.pk).get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % User)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User = User.objects.exclude(pk=self.instance.pk).get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)


class UserAuthenticationForm(UserCreationForm):

	
	class Meta:
		model = User
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")

