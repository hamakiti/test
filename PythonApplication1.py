
# 60日間使用可能なユーザに紐づいたTOKENを発行しておく
# https://developer.ciscospark.com/#
# 上記にログイン後右上のアイコンで自身のTOKENを確認

import requests

##自信のTOKENを変数として格納
access_code = 'MWU4NjRmN2EtMjVjZi00MTk3LWIwOTgtNWRhYTYzNGUzYzU2NDhhMmFhN2EtOGZl'
botDisplayName = 'Bot0@webex.bot'

##WebexTeamsからPOSTされたデータの受け取り
#投稿されたルームIDの取得
for line in json()["items"]:
    FromWebexTeams_RoomID = line["roomId"]

##特定したルームIDのスペースで投稿された文字列を取得
#requestsを投げるURLを格納
url = 'https://api.ciscospark.com/v1/messages'

#requestsで投げる情報
headers = {
    'Authorization' : 'Bearer ' + access_code,
    'Content-Type' : 'application/json'
}

#requestsで投げる情報
GetMessages_payload = {
    "roomId" : FromWebexTeams_RoomID,
    "max" : 1
}

#GetMessagesにrequestsで投げて帰ってきた結果を格納
GetMessages = requests.get(url,params = GetMessages_payload ,headers = headers)

#投稿されたメッセージの特定
for line in GetMessages.json()["items"]:
    PostMessages_text = line["text"]

##特定したメッセージをそのままBotで投稿する
#requestsで投げる情報
PostMessages_payload = {
    "roomId" : FromWebexTeams_RoomID,
    "text" : PostMessages_text
}

#PostMessagesにrequestsで投げて帰ってきた結果を格納
PostMessages = requests.get(url,json = PostMessages_payload ,headers = headers)