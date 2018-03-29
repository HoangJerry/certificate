from django.contrib import admin
from server.models import *
# Register your models here.

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'issuer', 'status', 'expires','exp')

class IpAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'owner',)

class UsageAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificate_id', 'ip_address')

admin.site.register(Certificate,CertificateAdmin)
admin.site.register(IpAddress,IpAddressAdmin)
admin.site.register(Usage,UsageAdmin)

