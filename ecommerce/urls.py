from django.urls import path, include

###from .views import SuperAdminView
from .views import (
	login_view, 
	logout_view,
	registration_view,
	home)

urlpatterns=[
path('home/',home, name='home' ),
    path('login/', login_view, name="normallogin"),
    path('logout/', logout_view, name="logout"),
    
    path('register/', registration_view, name="register"),
	
]
		

