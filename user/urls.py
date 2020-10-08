from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import UserViewSet,SignUpView

router = DefaultRouter()
router.register('users',UserViewSet,basename='user-list')

urlpatterns = [
    path('',include(router.urls)),
    path('signup/',SignUpView.as_view(),name='signup')
]