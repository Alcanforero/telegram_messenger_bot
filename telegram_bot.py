import requests
from config import TELEGRAM_SEND_MESSAGE_URL

class TelegramBot:
    def __init__(self):
        self.chat_id = None
        self.text = None

    def parse_webhook_data(self, data):
        message = data['message']
        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower()

    def action(self):
        success = None
        msg = self.incoming_message_text
        self.outgoing_message_text = msg
        success = self.send_message()
        return success

    def send_message(self):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))
        return True if res.status_code == 200 else False

    @staticmethod
    def init_webhook(url):
        requests.get(url)
