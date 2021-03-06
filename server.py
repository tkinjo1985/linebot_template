import os

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextSendMessage, TextMessage

app = Flask(__name__)

# Get the environment variables set in heroku Config Vars
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

# Set Authentication Information
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    """
    Check the request from the webhoo
    """
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    print(signature)
    print(type(signature))

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    print(type(body))

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


# ポート番号の設定
if __name__ == "__main__":
    #    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
