
# 60日間使用可能なユーザに紐づいたTOKENを発行しておく
# https://developer.ciscospark.com/#
# 上記にログイン後右上のアイコンで自身のTOKENを確認


if content_type == 'application/json':
      payload = request.body
else:
    payload = request.POST.get('payload')

signature = request.META.get('HTTP_X_HUB_SIGNATURE')

print(payload)
print(signature)

if signature:
    hasher = hmac.new(secret, payload, hashlib.sha1)
    logger.debug('Signature : {}'.format(signature))
    logger.debug('Calculated: sha1={}'.format(hasher.hexdigest()))













#import requests

# 自信のTOKENを変数として格納
#access_code = 'MWU4NjRmN2EtMjVjZi00MTk3LWIwOTgtNWRhYTYzNGUzYzU2NDhhMmFhN2EtOGZl'
#botDisplayName = 'Bot0@webex.bot'

# requestsを投げるURLを格納
#url = 'https://api.ciscospark.com/v1/messages'

# requestsで投げる情報
#headers = {
#    'Authorization' : 'Bearer ' + access_code,
#    'Content-Type' : 'application/json'
#}

# rにrequestsで投げて帰ってきた結果を格納
#r = requests.get(url, headers = headers)

#for line in r.json()["items"]:
#    Message_text = line["text"]

#Message_payload = {
#    "roomId": Message_ID,
    #Y2lzY29zcGFyazovL3VzL1JPT00vOGJkM2YwMjEtYjU2Yy0zOWI0LThjYzMtMTdlYmY3YmNlYzlh
#    "text": Message_text,
#}

#Message_space = requests.post(url, json = Message_payload, headers = headers)