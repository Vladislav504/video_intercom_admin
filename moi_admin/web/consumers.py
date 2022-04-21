import json
from channels.generic.websocket import AsyncWebsocketConsumer


class WebImageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("web", self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("web", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        image = text_data_json["message"]
        await self.channel_layer.group_send(
            "web", {"type": "intercom_message", "message": image}
        )

    async def intercom_message(self, event):
        image = event["message"]
        await self.send(text_data=json.dumps({"message": image}))


class WebTextConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("text", self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("text", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json["message"]
        await self.channel_layer.group_send(
            "text", {"type": "intercom_message", "message": text}
        )

    async def intercom_message(self, event):
        text = event["message"]

        await self.send(text_data=json.dumps({"message": text}))
