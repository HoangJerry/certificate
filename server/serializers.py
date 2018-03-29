from rest_framework import fields, serializers
from .models import *

class CertificateListSerializer(serializers.ModelSerializer):
    expires = serializers.IntegerField(read_only=True)
    
    class Meta():
        model = Certificate
        exclude = ('status',)
    
class IpAddressListSerializer(serializers.ModelSerializer):
    class Meta():
        model = IpAddress
        fields = '__all__'