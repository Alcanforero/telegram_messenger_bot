import requests
from flask import Flask, request, jsonify
from pymessenger.bot import Bot

from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL, FACEBOOK_ACCESS_TOKEN, FACEBOOK_VERIFY_TOKEN

app = Flask(__name__)

bot = Bot(FACEBOOK_ACCESS_TOKEN)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

@app.route("/facebook", methods=['GET'])
def start():
    token_sent = request.args.get("hub.verify_token")
    if token_sent == FACEBOOK_VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

@app.route("/facebook", methods=['POST'])
def recieve_message():
    output = request.get_json()
    for event in output['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response = message['message'].get('text')
                    bot.send_text_message(recipient_id, response)
    return "Message Processed"

@app.route('/telegram', methods=['POST'])
def index():
    req = request.get_json()
    bot = TelegramBot()
    bot.parse_webhook_data(req)
    success = bot.action()
    return jsonify(success=success)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
