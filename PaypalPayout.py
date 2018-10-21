import json
import random
from botocore.vendored import requests

def lambda_handler(event, context):



    headers = {
         'Content-Type': 'application/json',
      'Authorization': 'Bearer A21AAEu9ec0iDSYCHkAcSKQ5NBvNAMIiS6ZyiqlCYLes1YquTaSAltrrw9RU6m5apmA8uz87jngtsEuIKR9yxlttIYT1cED5Q'

    }


    payload = {
  "sender_batch_header": {
    "sender_batch_id": random.randint(1,101),
    "email_subject": "You have a payout!",
    "email_message": "You have received a payout! Thanks for using our service!"
  },
  "items": [
    {
      "recipient_type": "EMAIL",
      "amount": {
        "value": "15",
        "currency": "USD"
      },
      "note": "Thanks for your patronage!",
      "sender_item_id": "1",
      "receiver": "azizullah.parsa-facilitator@gmail.com"
    }
  ]
}

    url = 'https://api.sandbox.paypal.com/v1/payments/payouts'
    response = requests.post(url, headers=headers,
                             data=json.dumps(payload))
    response.raise_for_status()
    
    return {
        "statusCode": 200,
        "body": "payment completed"}


