from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

from . import models, serializers

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user")
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})





@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)





@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def certificates_list(request):
    if request.method == 'GET':
        certificates = models.Certificate.objects.all().order_by('-id')
        serializer = serializers.CertificateSerializer(certificates, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




@api_view(['GET', 'PUT', 'DELETE'])
def certificate_detail(request, pk):
    try:
        certificate = models.Certificate.objects.get(pk=pk)
    except models.Certificate.DoesNotExist:
        return Response('noCertificate')
    
    if request.method == 'GET':
        serializer = serializers.CertificateSerializer(certificate)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = serializers.CertificateSerializer(certificate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        certificate.delete()
        return Response('deleted')




@api_view(['POST'])
def copy_current_certificate(request, pk):
    # Fetch the existing certificate
    certificate = get_object_or_404(models.Certificate, pk=pk)
    
    # Get the data from the existing certificate
    certificate_data = serializers.CertificateSerializer(certificate).data
    
    # Update the name to indicate it's a copy
    new_name = f"{certificate.number} copied"
    certificate_data['number'] = new_name
    
    # Remove the primary key to avoid conflicts
    certificate_data.pop('id', None)
    
    # Create a new certificate with the same data
    new_certificate_serializer = serializers.CertificateSerializer(data=certificate_data)
    
    # Validate and save the new certificate
    if new_certificate_serializer.is_valid():
        new_certificate_serializer.save()
        return Response(new_certificate_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(new_certificate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response('')
    


    
