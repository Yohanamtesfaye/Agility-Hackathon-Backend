
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from user_app.models import Status
from safecityapi.serializers import UserRegisterSerializer, StatusSerializer,UserDetailSerializer

User = get_user_model()

# View for listing and creating users
@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny]) 
def createUserList(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        
        # Validate the data using the serializer
        if serializer.is_valid():
            # Save the user if data is valid
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Return errors if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for getting, updating, and deleting a user
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'GET':
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserDetailSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# View for listing and creating statuses
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])  # Only authenticated users can access this
def createStatusList(request):
    if request.method == 'GET':
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        
        # Validate the data before saving
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for getting, updating, and deleting a status
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])  # Only authenticated users can access this
def status_detail(request, pk):
    status_obj = get_object_or_404(Status, pk=pk)
    
    if request.method == 'GET':
        # Fetch and return the status details
        serializer = StatusSerializer(status_obj)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Update the status
        serializer = StatusSerializer(status_obj, data=request.data)
        
        # Validate the data before saving
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Delete the status
        status_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



