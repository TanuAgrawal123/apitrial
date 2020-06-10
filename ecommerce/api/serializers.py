from rest_framework import serializers
from ecommerce.models import User, Roles, Permission

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.exceptions import ValidationError

class RegistrationSerializer(serializers.ModelSerializer):

	password2= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username','full_name', 'password', 'password2','address','contactno',]
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		user = User(
					email=self.validated_data['email'],
					username=self.validated_data['username'],
					full_name=self.validated_data['full_name'],
					address=self.validated_data['address'],
					contactno=self.validated_data['contactno'],
					#groups=self.validated_data['groups']
					#photo=self.validated_data['photo']


				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		user.set_password(password)
		user.save()
		return user


class UserLoginSerializer(serializers.Serializer):
	token=serializers.CharField(read_only=True)
	email=serializers.EmailField()
	password=serializers.CharField(required=True,write_only=True)

	class Meta:
		model:User
		fields=['email',
		'password',
		
		'token',


		]
		extra_kwargs={
		"password":{"write_only":True}
		}
	

	def validate(self,data):
		user_obj=None
		email=data.get("email",None)
		Password=data["password"]
		if not email:
			raise ValidationError("Eamil is required")
		print(email)
		user=User.objects.filter(
			Q(email=email))
		print(user.exists())
		if user.exists() and user.count()==1:
			user_obj=user.first()
		else:
			raise ValidationError("This email is not valid")
		if user_obj:
			if not user_obj.check_password(Password):
				raise ValidationError("Incorrect credential")
		

		return data




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'full_name', 'username', 'email','gender', 'roles', 'contactno','address', 'password')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.is_active=	True
        user.save()

        return user


class PermissionSerializer(serializers.ModelSerializer):
	class  Meta:
		model= Permission
		fields='__all__'

class RolesSerializer(serializers.ModelSerializer):
	class Meta:
		model=Roles
		fields='__all__'






