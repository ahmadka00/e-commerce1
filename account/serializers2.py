from rest_framework import serializers
from account.models import UserBase


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = ['id', 'email', 'password']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserBase
        fields = ['user_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2', None)

        if password != password2:
            raise serializers.ValidationError({'Error': 'Password does not match'})


        if UserBase.objects.filter(email = attrs['email']).exists():
            raise serializers.ValidationError({'Error': 'Email already exist'})

        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserBase(**validated_data)
        user.set_password(password)
        user.save()
        return user
       