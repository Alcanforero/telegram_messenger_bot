FACEBOOK_ACCESS_TOKEN = 'EAAFWXhNGbZAkBAEIZAOJv2vFzz3g86fxfNt65JJsp5gmlCWhZAH6vgzpKUp0iCUheLhDufkLLGDQG1GFP5voPA8T0ZA4IakMldhoYAleae01DudbMco6gGJ6O0i1MUWsngt7NZAYo21J9NYZBNKiEK7ip04ZBUioh594mWDnzOLDAZDZD'
FACEBOOK_VERIFY_TOKEN = 'Messenger_Rasa_Test'

TELEGRAM_TOKEN = '1449014851:AAEM8DhsCCh9Su-7jsSdzdGqBwEVl61GhRo'

WEBHOOK_URL = 'https://telegram-messenger-bot.oa.r.appspot.com'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TELEGRAM_TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/telegram'.format(WEBHOOK_URL)

TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
