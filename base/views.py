from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import authenticate

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from base.models import *
from base.serializer import *


class ObtainToken(APIView):
    """
    API endpoint to obtain an authentication token for a user.
    """

    def post(self, request):
        serializer = ObtainTokenSerializer(data=request.data)
        if serializer.is_valid():
            # Attempt to authenticate user using the provided credentials
            user = User.objects.get(
                username=serializer.data["username"], 
                password=serializer.data["password"]
            )
            if user is not None:
                # If authentication succeeds, create a new token or reuse existing token
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class DataSentCreateView(APIView):
    """
    API endpoint to create and retrieve data sent by authenticated user.
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve all data sent by authenticated user
        data = Data_Sent.objects.filter(user=request.user)
        user_data = UserSerializer(request.user).data
        # Serialize the retrieved data and user information
        data_list = DataGetSerializer(data, many=True).data
        response_json = {'user': user_data, 'data': data_list}
        return Response(response_json)

    def post(self, request):
        # Retrieve authenticated user and user's IP address
        user = request.user
        ip_address = request.META.get('REMOTE_ADDR')
        if user.ip_address == str(ip_address):
            # Deserialize JSON data and assign user as the creator
            json_data = request.data
            json_data['user'] = user.pk
            # Validate serializer data and create new data object
            serializer = DataSentSerializer(data=json_data)
            if serializer.is_valid():
                data_sent = serializer.save()
                # Retrieve created data object and serialize it with DataCoolSerializer
                id = serializer.data['id']
                data = Data_Sent.objects.get(id=id)
                serializer = DataCoolSerializer(data)
                response_json = serializer.data
                return Response(response_json, status=status.HTTP_201_CREATED)   
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)


class UserCreateView(APIView):
    """
    API endpoint to create new user.
    """
    def post(self, request):
        # Deserialize JSON data and assign user's IP address
        json_data = request.data
        ip_address = request.META.get('REMOTE_ADDR')
        json_data['ip_address'] = ip_address
        # Validate serializer data and create new user object
        serializer = UserSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserResetIPView(APIView):
    """
    API endpoint to reset ip of user.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        ip_address = request.META.get('REMOTE_ADDR')
        # Check if the user's IP address is already set to the current IP address
        if user.ip_address != str(ip_address):
            # Update the user's IP address to the current IP address
            user.ip_address = ip_address
            user.save()
            # Return a success message
            return Response({"message": "IP address changed successfully."}, status=status.HTTP_200_OK)
        else:
            # Return a bad request response if the user's IP address is already set to the current IP address
            return Response({"error": "IP address is already set to the current IP address."}, status=status.HTTP_400_BAD_REQUEST)


class ChangeUserStatus(APIView):
    """
    API endpoint to change user status.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not request.user.is_superuser:
            return Response({"message": "You are not authorized to perform this action."}, status=403)

        serializer = ChangeUserStatusSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(id=serializer.data["user_id"])
            except User.DoesNotExist:
                return Response({"message": "User not found."}, status=404)

            user.is_staff = True
            user.save()

            return Response({"message": "User status changed successfully."}, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RemoveDataSentOBJ(APIView):
    """
    API endpoint to delete data_sent objects.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        objects = Data_Sent.objects.filter(user=request.user.pk)
        objects.delete()
        return Response({"message": "Removed Data Sent Objects."}, status=200)


class RemoveDataSentOBJ_ID(APIView):
    """
    API endpoint to delete data_sent object by id
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RemoveOBJ_IDSerializer(data=request.data)
        if serializer.is_valid():
            object = Data_Sent.objects.get(user=request.user.pk,id=serializer.data["id"])
            object.delete()
            return Response({"message": "Removed Data Sent Objects."}, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)