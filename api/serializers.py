from rest_framework import serializers
from django.contrib.auth.models import User


from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = '__all__'





class CertificateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = models.Certificate
        fields = '__all__'



