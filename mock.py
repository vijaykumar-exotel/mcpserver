import requests
import subprocess
import json

url = "https://api.in.exotel.com/v1/Accounts/ameyo5m/Sms/send.json"

payload = {'From': '+912247788868',
'To': '+919899028650',
'Body': 'This is a test message powered by Exotel.',
'EncodingType': '',
'DltTemplateId': '',
'DltEntityId': '',
'SmsType': '',
'Priority': '',
'StatusCallback': '',
'CustomField': '',
'ShortenUrl': '',
'ShortenUrlParams[Tracking]': '',
'ShortenUrlParams[ClickTrackingCallbackUrl]': ''}

headers = {
  'Authorization': 'Basic e3tBdXRoS2V5fX06e3tBdXRoVG9rZW59fQ==',
  'Content-Type' : 'application/json'
}

#response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)


#https://<your_api_key>:<your_api_token><subdomain>/v2/accounts/<your_sid>/messages


url = "https://399117e47411d9f0f9120de1181323056e55b88c664d2f67:80711a9d4562955dc3591f1ada24790f3b5088dbaa3263db@api.in.exotel.com/v2/accounts/ameyo5m/messages"

payload = {'whatsapp':{"messages" : {"from":"+912247788868","to":"+919899028650","content": {"recepient_type":"individual","type":"Text","text":{"body":"Hi, This is test message."}}}}}

headers = {
  'Authorization': 'Basic e3tBdXRoS2V5fX06e3tBdXRoVG9rZW59fQ==',
  'Content-Type' : 'application/json'
}

#response = requests.request("POST", url, data=payload)

#print(response.text)




url = "https://399117e47411d9f0f9120de1181323056e55b88c664d2f67:80711a9d4562955dc3591f1ada24790f3b5088dbaa3263db@api.in.exotel.com/v1/Accounts/ameyo5m/Calls/connect.json?From=09899028650&Url=http://my.in.exotel.com/ameyo5m/exoml/start_voice/24049&CallerId=02247788868"
headers = {
  'Authorization': 'Basic e3tBdXRoS2V5fX06e3tBdXRoVG9rZW59fQ==',
  'Content-Type' : 'application/json'
}
#response = requests.request("POST", url, headers=headers)


#print(response.text)


data = '{"title":"foo","body":"bar","userId":1}'
headers = ["-H", "Content-Type: application/json"]

#result = subprocess.run(
#    ["curl", "-s", "-X", "POST", url] + headers ,
#    capture_output=True,
#    text=True
#)

#print(result.stdout)



number = "+919899028650"
url = "https://399117e47411d9f0f9120de1181323056e55b88c664d2f67:80711a9d4562955dc3591f1ada24790f3b5088dbaa3263db@api.in.exotel.com/v2/accounts/ameyo5m/messages"
data = {
    "custom_data": "Order12",
    "status_callback": "https://webhook.site",
    "whatsapp": {
        "messages": [
            {
                "custom_data": "Order12",
                "status_callback": "https://webhook.site",
                "from": "+912247788868",
                "to": number,
                "content": {
                    "recipient_type": "individual",
                    "type": "text",
                    "text": {
                        "preview_url": False,
                        "body": "I am Saurabh, your personal assistant, wanted to get in touch with you for an exciting offer. Please let me know if we can talk."
                    }
                }
            }
        ]
    }
}

json_data = json.dumps(data)

command = [
    "curl",
    "-X", "POST",
    url,
    "-H", "Content-Type: application/json",
    "-d", json_data
]


# Run the command and capture the output
result = subprocess.run(command, capture_output=True, text=True)

print(result.stdout)
