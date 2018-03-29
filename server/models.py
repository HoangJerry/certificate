from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your models here.

class Certificate(models.Model):
    STATUS_VALID = 0
    STATUS_RENEW = 10
    STATUSES = (
        (STATUS_VALID, _("Valid")),
        (STATUS_RENEW, _("Renew")),
    )

    name = models.CharField(max_length=200,null=True, blank=True)
    issuer = models.CharField(max_length=200,null=True, blank=True)
    status = models.SmallIntegerField(choices=STATUSES, default=STATUS_VALID)
    expires = models.IntegerField(default=0)
    
    def __str__(self):      
        return str(self.id)

    @property
    def exp(self):
        return datetime.datetime.fromtimestamp(self.expires/1000.0)


class IpAddress(models.Model):
    ip_address = models.CharField(max_length=200, primary_key=True)
    owner = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):      
        return self.ip_address
    
class Usage(models.Model):
    certificate_id = models.ForeignKey(Certificate)
    ip_address = models.ForeignKey(IpAddress)
  


