from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
import re
import html


class MySynconsumer(WebsocketConsumer):
    def connect(self):
        print('connection connected....')
        self.group_name = self.scope['url_route']['kwargs']['grpname']
        groupname_sanitized = re.sub(r"[^\w.-]", "", self.group_name)
        groupname_sanitized = groupname_sanitized[:100]
        self.group_name = groupname_sanitized

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
    def receive(self, text_data=None, bytes_data=None):
        # print('data recive....',text_data)
        data = json.loads(text_data)
        data['name'] = sanitize_name(data['name'])
        # message  = data['msg']
        # print("actual messgae ",message)

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat.message',
                'message': data['msg'],
                'name' : data['name'],
            })
    
    def chat_message(self, event):
        message = event['message']
        print('message........',message)
        self.send(text_data=json.dumps({
            'msg': message,
            'name' : event['name'],
        }))
    
    def disconnect(self, code):
        print('conection close....')
    


# Xss protection
def sanitize_name(name):
    sanitized_name = html.escape(name)
    if name != sanitized_name:
        return "Invalid name"
    return sanitized_name