from django.urls import path,include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from ecommerce.api.views import(
registeration_view, RegisterationDetailView, UserViewSet, login ,LogoutView ,PermissionViewSet,  RolesViewSet
	)
router = DefaultRouter()
router.register('user', UserViewSet)

router.register('permission', PermissionViewSet)
router.register('roles',RolesViewSet)
urlpatterns=[
path('', include(router.urls)),
path('register',registeration_view, name='register'),
path('registerdetail/<int:pk>', RegisterationDetailView.as_view()),
path('account/logout/', LogoutView.as_view(), name='logout'),
path('account/login/', login, name='login'),


]

