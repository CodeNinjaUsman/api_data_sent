from base.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # Serializer for the User model
    class Meta:
        model = User
        fields = '__all__'

class DataCoolSerializer(serializers.ModelSerializer):
    # Serializer for the Data_Sent model, including the related User model
    user = UserSerializer()
    class Meta:
        model = Data_Sent
        fields = ['id', 'created', 'data','user']

class DataSentSerializer(serializers.ModelSerializer):
    # Serializer for the Data_Sent model
    class Meta:
        model = Data_Sent
        fields = ['id', 'created', 'data','user']

class DataGetSerializer(serializers.ModelSerializer):
    # Serializer for the Data_Sent model, used to retrieve data for a specific user
    class Meta:
        model = Data_Sent
        fields = ['id', 'created', 'data']

class ObtainTokenSerializer(serializers.Serializer):
    # Serializer for obtaining a token
    username = serializers.CharField()
    password = serializers.CharField()

class ChangeUserStatusSerializer(serializers.Serializer):
    # Serializer for changing a user's status to staff
    user_id = serializers.IntegerField()

class RemoveOBJ_IDSerializer(serializers.Serializer):
    # Serializer for deleting data sent objects by id
    id = serializers.IntegerField()