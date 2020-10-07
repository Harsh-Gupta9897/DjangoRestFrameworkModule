from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from user.permission import IsAdmin ,IsStudentorAdminorTeacher, IsTeacherorAdmin,AllowAny
from user.models import User
from user.serializers import UserSerializer


# Create your views here.

class UserViewSet(ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = []
    def get_permissions(self):
        permission_classes = []
        #creation of user 
        if self.action == 'create':
            permission_classes = [IsTeacherorAdmin,]
        #to list all the students and teachers on the basis of permissions
        elif self.action == 'list':
            permission_classes = [IsStudentorAdminorTeacher]
        # to update values by autheticated user 
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsTeacherorAdmin]
        # to destroy the user account of students or teacher by admin
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        
        return [permission() for permission in permission_classes]
    
    # for filtering queries on the basis of priorities
    def get_queryset(self):
        group = self.request.user.groups.id
        print(group)
        if group == 2:
            query =User.objects.filter(groups_id=3)
            return query

        if group == 3:
            return User.objects.filter(pk=self.request.user.id)

        if group == 1:
            return User.objects.all()


# class SignUpView()