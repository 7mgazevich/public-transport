import requests
import sys
def test_slack():
    url = "https://slack.com/api/chat.postMessage"
    channel = "C6ET17F7B"
    token = "xoxp-157391333303-219490411730-240312548326-ef40af134c777816ac8b69a332e7b869"
    text = "Good night"
    payload = {'channel': channel, 'token': token, 'text': text}
    response = requests.post(url, data=payload)
    print(response.json())

