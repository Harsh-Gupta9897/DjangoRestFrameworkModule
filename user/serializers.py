from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from user.models import User

# for creating ,updating,deleting user on the baiss of permissions serializer for user model 
class UserSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = False
        user.save()

        return user

  