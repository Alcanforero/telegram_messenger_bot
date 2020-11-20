import requests
from flask import Flask, request, jsonify
from pymessenger.bot import Bot

from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL, FACEBOOK_ACCESS_TOKEN, FACEBOOK_VERIFY_TOKEN

app = Flask(__name__)

bot = Bot(FACEBOOK_ACCESS_TOKEN)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/telegram', methods=['POST'])
def index():
    req = request.get_json()
    bot = TelegramBot()
    bot.parse_webhook_data(req)
    success = bot.action()
    return jsonify(success=success)

@app.route("/facebook", methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + FACEBOOK_ACCESS_TOKEN, json=data)
    print(resp.content)
 
 
@app.route('/facebook', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']

    #Llamar a método que gener la respuesta y pasarlo por parámetro message a la siguiente llamada:
    reply(sender, message)
 
    return "ok"

if __name__ == "__main__":
    app.run(port=5000, debug=True)