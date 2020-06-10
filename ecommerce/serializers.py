from rest_framework import serializers
###from .models import Admin, SuperAdmin, SubAdmin










"""class SuperAdminSerializer(serializers.ModelSerializer):
	class Meta:
		model=SuperAdmin
		fields=['user','Name', 'Email', 'Gender']



class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model=Admin
		fields=['user','Name', 'Email', 'Gender']


class SubAdminSerializer(serializers.ModelSerializer):
	class Meta:
		model=SubAdmin
		fields=['user','Name', 'Email', 'Gender']

		

		