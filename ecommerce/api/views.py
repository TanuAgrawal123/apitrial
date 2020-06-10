
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from ecommerce.api.serializers import RegistrationSerializer, UserLoginSerializer, UserSerializer, PermissionSerializer, RolesSerializer
from ecommerce.models import User, Permission, Roles
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.status import  HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from django.contrib.auth import login as django_login
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
@api_view(['POST','GET'])
def registeration_view(request):
	serializer_class=RegistrationSerializer
	
	if request.method=='POST':
		serializer=RegistrationSerializer(data=request.data)
		data={}
		if serializer.is_valid():
			user=serializer.save()
			
			data['response']="successfully registered a new user"
			data['email']=user.email
			data['username']=user.username
			data['full_name']=user.full_name
			data['contactno']=user.contactno
			data['address']=user.address
			
			
			#data['groups']=user.groups
			django_login(request,user)
			#data['photo']=user.photo
		else:
			data=serializer.errors
		return Response(data)
	if request.method=='GET':
		data=User.objects.all()
		serializer=RegistrationSerializer(data, many=True)
		return Response(serializer.data)

class RegisterationDetailView(APIView):
	serializers_class=RegistrationSerializer
	
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404
	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = RegistrationSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = RegistrationSerializer(user, data=request.data)
		data={}

		if serializer.is_valid():
			user=serializer.save()
			data['response']="successfully made the changes"
			data['username']=user.username
			data['email']=user.email
			data['full_name']=user.full_name
			data['contactno']=user.contactno
			data['address']=user.address
			#data['photo']=user.photo
			
		else:
			data=serializer.errors

		return Response(data)
		
	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PermissionViewSet(ModelViewSet):
	queryset=Permission.objects.all()
	serializer_class=PermissionSerializer
class RolesViewSet(ModelViewSet):
	queryset=Roles.objects.all()
	serializer_class=RolesSerializer

"""class LoginView(APIView):
    serializer_class = AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request)

"""
class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response("successfully logged out", status=HTTP_200_OK)

"""
class UserLoginAPIView(APIView):
	permission_classes=[AllowAny]
	authentication_classes=[TokenAuthentication]
	serializer_class=UserLoginSerializer

	def post(self, request, *args, **kwargs):
		data=request.data
		serializer=UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data=serializer.data
			
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
"""

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

