import json
import pytest
import asyncio

from autobahn.asyncio.websocket import (
    WebSocketClientProtocol,
    WebSocketClientFactory,
)

@pytest.fixture
def websocket_client(event_loop, unused_tcp_port):

    class ClientProtocol(WebSocketClientProtocol):
        def sendJsonMessage(self, data):
            msg = json.dumps(data)
            self.sendMessage(bytes(msg, 'UTF-8'))
        def onConnect(self, response):
            pass
        async def onOpen(self):
            self.sendJsonMessage({'event':'init'})
        def onMessage(self, payload, isBinary):
            body = json.loads(payload.decode('utf-8'))
            if body.get('name') == 'init':
                self.sendJsonMessage({'event':'load'})
        def onClose(self, *args):
            pass

    class Client(object):
        def __init__(self):
            self.factory = WebSocketClientFactory(u"ws://127.0.0.1:{}".format(unused_tcp_port))
            self.factory.protocol = ClientProtocol
            self.port = unused_tcp_port
        async def connect(self):
            self.transport, self.protocol = await event_loop.create_connection(
                self.factory,
                '127.0.0.1',
                unused_tcp_port,
            )
        async def close(self):
            self.protocol.sendClose()
        def sendJsonMessage(self, data):
            self.protocol.sendJsonMessage(data)

    return Client()
