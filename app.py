from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('d+k3AQE2R8T29GRA0WfV0FwaP1o1jtMYHWLslkfAxVjtjADhWZu/YuTpDA5b0LY3PmmLi/HacFqXTW2FVMWPe54PhQ4fX/YKpC6rNZLsVtAOj8aOQB4Zs9QpIGGRuN8IRhAP26p708f871ToxuYmzQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0333a91e90ec7a4d8b36bfaa8fa107ad')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉你在問什麼?"

    if msg == 'hi':
        r ='hi'
    elif msg == '你吃飽了沒?':
        r ='還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()