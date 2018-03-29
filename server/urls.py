from django.conf.urls import url
from . import views
from . import models

urlpatterns = [
	url(r'^certificates/$', views.CertificateList.as_view(), name='certificates'),
	url(r'^certificates/renew/$', views.CertificateRenew.as_view(), name='certificates'),
	url(r'^certificates/(?P<pk>[0-9]+)/$', views.CertificateDetail.as_view(), name='certificate'),
	url(r'^ip_addresses/$', views.IpAddresses.as_view(), name='ipaddresses'),

]