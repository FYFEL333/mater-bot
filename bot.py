import requests
import time

TOKEN = '7779321284:AAGDajr7R8QZNnN0UzdnTr_V65Gn-XMRsb4'
URL = f'https://api.telegram.org/bot{TOKEN}/'
offset = None

# Все команды и фразы
commands = {
    "lesh": "дал леща ✋",
    "udar": "прописал в ебыч с кулака 👊",
    "kickhard": "уебал с ноги в живот 🦶",
    "cuff": "надел(а) наручники на 😏⛓️‍💥",
    "kiss": "поцеловал(а) 💋",
    "kick": "пнул(а) 🦵",
    "hug": "обнял(а) 🤗",
    "slap": "шлёпнул(а) по попе ✋🍑",
    "bite": "укусил(а) за руку 😁🤙",
    "stare": "уставился(лась) с подозрением на 😑",
    "cry": "зарыдал(а) на плече у 😭",
    "boom": "взорвал(а) с криком «BOOM!»",
    "troll": "затроллил(а)",
    "pray": "помолился(ась) за 🙏",
    "respect": "выразил(а) уважение 👍🏻",
    "pat": "погладил(а) по голове 🫳🙂‍↕️",
    "traxnut": "трахнул(а) 😏🔞",
    "plunut": "плюнул(а) в ебло 💦",
    "kastrirovat": "кастрировал(а) ✂️",
    "vrot": "дал(а) в рот 🍆👄",
    "obossal": "обоссал(а) 💦",
    "grud": "пожамкал грудь 🫴🍒"
}

def get_updates():
    global offset
    response = requests.get(URL + 'getUpdates', params={'offset': offset, 'timeout': 30})
    return response.json()['result']

def send_message(chat_id, text, reply_to=None):
    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_to_message_id': reply_to
    }
    requests.post(URL + 'sendMessage', data=data)

def handle_message(message):
    global commands

    if 'text' not in message:
        return

    text = message['text']
    chat_id = message['chat']['id']
    from_user = message['from']['first_name']
    reply_to = message.get('reply_to_message')

    if not reply_to:
        return  # команда работает только как reply

    to_user = reply_to['from']['first_name']

    if text.startswith('/'):
        command = text[1:].split()[0]
        if command in commands:
            action_text = commands[command]
            response = f"{from_user} {action_text} {to_user}"
            send_message(chat_id, response, reply_to=message['message_id'])

def main():
    global offset
    print("Bot started...")
    while True:
        updates = get_updates()
        for update in updates:
            offset = update['update_id'] + 1
            message = update.get('message')
            if message:
                handle_message(message)
        time.sleep(1)

if __name__ == '__main__':
    main()
