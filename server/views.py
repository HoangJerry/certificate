from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.

def IndexPage(request):
    return render(request, 'angular/index.html', {})
    
class CertificateList(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer
    
class CertificateDetail(generics.RetrieveUpdateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer

class CertificateRenew(APIView):
    
    def post(self, request, format=None):
        certificate = Certificate.objects.filter(id=request.data.get('id'))[0]
        certificate.expires += 94670778000 # 3 years
        certificate.save()
        return Response({'status':1})

class IpAddresses(generics.ListAPIView):
    queryset = IpAddress.objects.all()
    serializer_class = IpAddressListSerializer

    def get_queryset(self):
        certificate_id = self.request.GET.get('certificate_id',None)
        if certificate_id:
            ret = Usage.objects.values_list('ip_address',flat=True).filter(certificate_id=certificate_id)
            return IpAddress.objects.filter(ip_address__in=ret)
        return IpAddress.objects.all()



    