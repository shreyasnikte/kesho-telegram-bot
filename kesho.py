import telegram
import json
import requests
import time
import urllib

import utils
import stream


TOKEN = utils.token()
URL = "https://api.telegram.org/bot{}/".format(TOKEN)



class Features(object):
    def __init__(self):
        pass

    def music(self, updates):
        for update in updates["result"]:
            try:
                text = update["message"]["text"]
                if (text == "Stop" or text =="stop"):
                    self.player.stop()
                    continue

                elif (text == "Pause" or text =="pause"):
                    self.player.pause()
                    continue

                elif text== "Play":
                    self.play()
                    continue


                self.player, title = stream.yt(text)
                text = "Playing " + title + " from Youtube"
            
            
            except:
                text = "Format not supported. Try text message"
            

            try:
                chat = update["message"]["chat"]["id"]
            except:
                chat = update["edited_message"]["chat"]["id"]
            send_message(text, chat)




def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)




def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)



# def controlButtons(update):
#     keyboard = [[InlineKeyboardButton("Apples", callback_data='1')],
#         [InlineKeyboardButton("Oranges", callback_data='2')],
#         [InlineKeyboardButton("Beans", callback_data='3')],
#         [InlineKeyboardButton("Rice", callback_data='4')],
#         [InlineKeyboardButton("Bread", callback_data='5')],                
#         [InlineKeyboardButton("Tomatos", callback_data='6')],                
#         [InlineKeyboardButton("Strawberry", callback_data='7')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Multiple choice Quizz \nSelect all vegetables:', reply_markup=reply_markup)




def main():
    utils.init()
    last_update_id = None
    features = Features()
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            features.music(updates)
            controlButtons(updates["result"])
        time.sleep(0.5)


if __name__ == '__main__':
    main()