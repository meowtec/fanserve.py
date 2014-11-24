# coding:utf-8
import hashlib
import json
import urllib
import abc


class Core():
    receive_text = None
    receive_event = None
    receive_default = None
    app_secret = None

    def post(self):
        auth_result = self.__authentication()
        if auth_result is False:
            return False

        body_data = json.loads(self.body_raw())
        self.body_data = body_data
        msg_type = body_data.get('type')
        msg_text = body_data.get('text')

        if msg_type == 'text' and self.receive_text:
            self.receive_text(msg_text)

        elif msg_type == 'event' and self.receive_event:
            event_type = body_data['data']['subtype']
            self.receive_event(event_type)

        elif self.receive_default:
            self.receive_default(body_data)

    def get(self):
        auth = self.__authentication()
        if auth is True:
            self.write(self.__safe_get_argument('echostr'))

    def __safe_get_argument(self, name):
        try:
            value = self.get_argument(name)
        except:
            value = None
        return value

    def __authentication(self):
        timestamp = self.__safe_get_argument('timestamp')
        nonce = self.__safe_get_argument('nonce')
        signature_str = self.__create_signature([self.app_secret, timestamp, nonce])
        if signature_str == self.__safe_get_argument('signature'):
            return True
        else:
            return False

    # 可以在子类中调用的方法
    def reply(self, msg_type, data):
        send_data = {
            "result": True,
            "receiver_id": self.body_data['sender_id'],
            "sender_id": self.body_data['receiver_id'],
            "type": msg_type
        }
        encode_data = urllib.quote(json.dumps(data))
        send_data['data'] = encode_data
        self.write(json.dumps(send_data))

    def reply_text(self, text):
        self.reply(msg_type='text', data={'text': text})

    @staticmethod
    def __create_signature(message_arr):
        message_arr.sort()
        join_str = ''.join(message_arr)
        return hashlib.sha1(join_str).hexdigest()

    @abc.abstractmethod
    def body_raw(self):
        pass

    @abc.abstractmethod
    def get_argument(self, name):
        pass

    @abc.abstractmethod
    def write(self, text):
        pass