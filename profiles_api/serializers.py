from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """
    Serializes a name field for testing our APIView
    """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializes a user profile object
    Model Serializer for defining the meta class
    point to a model
    """
    class Meta:
        # Sets up to point to UserProfile model
        model = models.UserProfile
        # Need to define the field accessible to our serializers to our API. Add exception to password since it is required during password creation
        # Not allow password hash
        fields = ('id','email','name','password')
        extra_kwargs = {
        'password': {
            'write_only':True,
            'style':{'input_type':'password'}
            }
        }

    # Overwrite the create serializer. Usually uses default
    # This is for the hashed password which is in the user function. Default would show it as normal text.
    def create(self,validated_data):
        """ Create and return a new user"""
        user = models.UserProfile.objects.create_user(
        email = validated_data['email'],
        name = validated_data['name'],
        password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
