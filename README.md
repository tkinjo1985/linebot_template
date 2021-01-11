# LINE Messaging APIを使ったオウム返しBOT

HerokuとLINE Messaging APIを組み合わせオウム返しBOT

オウム返しを行っているコード

```server.py
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
```

# Herokuへのデプロイ方法.
LINE Messaging APIを使用する準備は事前に済ませておく。


1. Herokuのアカウントを登録する。
2. Herokuに新しいAPPを追加する。
3. Heroku CLIをインストールする。

macOSの場合
```bash
$ brew tap heroku/brew && brew install heroku
```

その他のOSは
[The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)を参照する。

4. Heroku Gitを使う場合

```
# Herokuにログインする
$ heroku login
$ git init
$ heroku git:remote -a [2で作成したAPP名]
```

5. ２で作成したAPPのdashboardのSettings - Config Varsを選択し下記のKEY:VALUEを追加する。
```
YOUR_CHANNEL_ACCESS_TOKEN : LINE Messaging APIのChannel access token

YOUR_CHANNEL_SECRET : LINE Messaging APIのChannel secret
```

6. git pushでデプロイすることができる。
```
$ git add .
$ git commit -am "コミットメッセージ"
$ git push heroku master
```

GitHubを使ってデプロイしたい場合はAPPのdashboardのDeployの項目からGitHubのリポジトリを連携される。
