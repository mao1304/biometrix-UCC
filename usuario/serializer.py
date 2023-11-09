from rest_framework import serializers
from .models import NewUser

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields= ('username', 'password', 'admin_check',) 
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields= ('username', 'password', 'first_name', 'last_name','huella', 'admin_check',) 