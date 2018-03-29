
from channels_api.bindings import ResourceBinding
from channels.binding.websockets import WebsocketBinding
from channels_api.decorators import detail_action, list_action
from pprint import pprint
from django.core.paginator import Paginator
from certificates import settings
from .models import *
from .serializers import CertificateListSerializer

class CertificateBinding(ResourceBinding):
    model = Certificate
    stream = "status"
    serializer_class = CertificateListSerializer
    queryset = Certificate.objects.all()
