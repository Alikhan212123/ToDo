from rest_framework import serializers
import re

from apps.users.models import User
from apps.todo.serializers import TaskSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "phone_number", "created_at", "age")

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255, write_only=True,
    )
    password2 = serializers.CharField(
        max_length = 255, write_only=True,
    )

    class Meta:
        model = User 
        fields = ('username', 'email', 'phone_number', 'age', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email = self.initial_data.get("email"),
            phone_number = self.initial_data.get("phone_number"),
            age = self.initial_data.get("age"),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserDetail(serializers.ModelSerializer):
    user_delete = TaskSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'age','user_delete')




    # def validate(self, values):
    #     if values['phone_number'] != '+996':
    #         raise serializers.ValidationError({'phone_number : Начните номер телефона с +996'})
    #     return values

    # def validate(self, attrs):
    #     phone_regex = re.compile(r'^\+996\d{9}$')
    #     if not phone_regex.match(attrs['username']):
    #         raise serializers.ValidationError('Номер телефона должен быть в формате +996XXXXXXXXX')
    #     return super().validate(attrs)