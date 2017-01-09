import pytest
import asyncio

from sofi.app import Sofi
from sofi.ui import View, Container, ButtonGroup, Button


def key_for_callback(cb):
    return str(id(cb))

def check_callback_ids(app):
    for event in app.interface.handlers.keys():
        for key in app.interface.handlers[event].keys():
            if key == '_':
                continue
            for cb in app.interface.handlers[event][key]:
                assert key_for_callback(cb) == key

@pytest.mark.asyncio
async def test_unregister(websocket_client):

    app = Sofi(port=websocket_client.port)

    clicks_received = []

    async def oninit(e):
        v = View()
        c = Container()
        b = Button()
        c.addelement(b)
        v.addelement(c)
        app.load(str(v))

    async def onload(e):
        app.register('click', onclick1, 'button')
        app.register('click', onclick2, 'button')

    async def onclick1(e):
        clicks_received.append(e)
        await asyncio.sleep(.5)
        app.unregister('click', onclick2, 'button')

    async def onclick2(e):
        clicks_received.append(e)


    app.register('init', oninit)
    app.register('load', onload)


    await app.server.server
    await websocket_client.connect()
    await asyncio.sleep(2)
    check_callback_ids(app)
    # app.register('click', onclick, 'button')
    # app.unregister('click', onclick, 'button')
    websocket_client.sendJsonMessage({'event':'click', 'key':key_for_callback(onclick1)})
    websocket_client.sendJsonMessage({'event':'click', 'key':key_for_callback(onclick2)})
    await asyncio.sleep(1)
    check_callback_ids(app)
    assert len(clicks_received) == 2

    app.unregister('click', onclick1, 'button')
    assert onclick1 not in app.interface.handlers['click'].get(key_for_callback(onclick1), [])
    assert onclick2 not in app.interface.handlers['click'].get(key_for_callback(onclick2), [])
    await websocket_client.close()



@pytest.mark.asyncio
async def test_function_callbacks(websocket_client):

    NUM_BUTTONS = 8

    app = Sofi(port=websocket_client.port)

    async def oninit(e):
        print('oninit')
        v = View()
        c = Container()
        bg = ButtonGroup()
        for i in range(NUM_BUTTONS):
            b = Button(text='Button {}'.format(i), attrs={'id':'btn_{}'.format(i)})
            bg.addelement(b)
        c.addelement(bg)
        v.addelement(c)
        app.load(str(v))

    async def onload(e):
        print('onload')
        app.register('click', onclick, 'button')
        #check_callback_ids(app)

    async def onclick(e):
        btn_text = e['event_object']['target']['innerText']
        print('onclick: {}'.format(btn_text))
        #check_callback_ids(app)

    app.register('init', oninit)
    app.register('load', onload)


    await app.server.server
    await websocket_client.connect()
    await asyncio.sleep(2)
    check_callback_ids(app)
    await websocket_client.close()


@pytest.mark.asyncio
async def test_instance_method_callbacks(websocket_client):

    class MyApp(object):
        NUM_BUTTONS = 8
        def __init__(self):
            self.app = Sofi(port=websocket_client.port)
            self.app.register('init', self.oninit)
            self.app.register('load', self.onload)
        async def oninit(self, e):
            print('oninit')
            v = View()
            c = Container()
            bg = ButtonGroup()
            for i in range(self.NUM_BUTTONS):
                b = Button(text='Button {}'.format(i), attrs={'id':'btn_{}'.format(i)})
                bg.addelement(b)
            c.addelement(bg)
            v.addelement(c)
            self.app.load(str(v))
        async def onload(self, e):
            print('onload')
            self.app.register('click', self.onclick, 'button')
            #check_callback_ids(self.app)
        async def onclick(self, e):
            btn_text = e['event_object']['target']['innerText']
            print('onclick: {}'.format(btn_text))
            #check_callback_ids(self.app)

    my_app = MyApp()

    await my_app.app.server.server
    await websocket_client.connect()
    await asyncio.sleep(2)
    check_callback_ids(my_app.app)
    await websocket_client.close()
