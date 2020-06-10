from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser, AbstractUser
	)
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

gender=[('male','male'),('female', 'female')]



class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			full_name=full_name,
			contactno=contactno,
			address=address,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	


class Permission(models.Model):
	name=models.CharField(max_length=100, null=True, unique=True)

	def __str__(self):
		return self.name

class Roles(models.Model):
	name=models.ForeignKey(Group, on_delete=models.CASCADE)
	permission=models.ManyToManyField(Permission)

	def __str__(self):
		return self.name.Name



class User(AbstractUser):
	email=models.EmailField(max_length=255, unique=True)
	full_name=models.CharField(max_length=255)
	gender=models.CharField(choices=gender, max_length=10, default='male')
	contactno=models.CharField(max_length=20, null=True)
	address=models.CharField(max_length=100)
	#photo=models.ImageField(null=True)
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)
	is_admin=models.BooleanField(default=False)
	is_superuser=models.BooleanField(default=False)

	date_joined=models.DateTimeField(auto_now_add=True, null=True)
	roles=models.ForeignKey(Roles, on_delete=models.CASCADE, null=	True)

	#USERNAME_FIELD='email'
	objects=MyAccountManager()

	REQUIRED_FIELDS=['email']

	

	
 



	def get_full_name(self):
		return self.full_name

	def __str__(self):
		return self.username
	
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)



