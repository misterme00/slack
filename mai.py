import os
import slack

client = slack.WebClient(token='xoxb-910226802273-908949284947-B5eF2rx5omNzvs7p0U5RgRBb')

response = client.chat_postMessage(
    channel='#random',
    text="Hello world!")
#assert response["ok"]
#assert response["message"]["text"] == "Hello world!"
#channels = client.conversations_list()
print(response)
res = client.chat_postMessage(
  channel="CT2CLGNTX",
  blocks=[
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Danny Torrence left the following review for your property:"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room " +
            "237 was far too rowdy, whole place felt stuck in the 1920s."
        },
        "accessory": {
            "type": "image",
            "image_url": "https://images.pexels.com/photos/750319/pexels-photo-750319.jpeg",
            "alt_text": "Haunted hotel image"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Average Rating*\n1.0"
            }
        ]
    }
  ]
)
print(res)