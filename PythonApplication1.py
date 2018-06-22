
# 60日間使用可能なユーザに紐づいたTOKENを発行しておく
# https://developer.ciscospark.com/#
# 上記にログイン後右上のアイコンで自身のTOKENを確認

import requests

# 自信のTOKENを変数として格納
access_code = 'MWU4NjRmN2EtMjVjZi00MTk3LWIwOTgtNWRhYTYzNGUzYzU2NDhhMmFhN2EtOGZl'
botDisplayName = 'Bot0@webex.bot'

# requestsを投げるURLを格納
url = 'https://api.ciscospark.com/v1/messages'

# requestsで投げる情報
headers = {
    'Authorization' : 'Bearer ' + access_code,
    'Content-Type' : 'application/json'
}

# rにrequestsで投げて帰ってきた結果を格納
r = requests.get(url, headers = headers)

for line in r.json()["items"]:
    Message_text = line["text"]

Message_payload = {
    "roomId": Message_ID,
    "text": Message_text,
}

Message_space = requests.post(url, json = Message_payload, headers = headers)