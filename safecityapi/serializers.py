
from rest_framework import serializers
from django.contrib.auth import get_user_model
from user_app.models import Status


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(required=True)  


    class Meta:
        model = User
        fields = ['id','name', 'email','phone_number', 'password', 'password_confirmation']

    def validate(self, data):
        # Check if password and password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": "Passwords do not match."})
        if User.objects.filter(phone_number=data['phone_number']).exists():
            raise serializers.ValidationError({"phone_number": "A user with this phone number already exists."})
        return data
    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data.get('name', ''),
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),

        )
        return user
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'name', 'userName', 'phone_number','email','gender', 'location', 'role'
        ]  
          

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'owner', 'status_type', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']  

        