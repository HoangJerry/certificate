from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class
from channels.routing import route

from server.bindings import CertificateBinding
from server.consumers import ws_add, ws_message, ws_disconnect

class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'status': CertificateBinding.consumer
    }

channel_routing = [	
    route_class(APIDemultiplexer),
    # route("websocket.connect", ws_add),
    # route("websocket.receive", ws_message),
    # route("websocket.disconnect", ws_disconnect),
    # route("http.request", "api.consumers.http_consumer"),
]
