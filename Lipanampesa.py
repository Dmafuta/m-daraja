
import requests
from requests.auth import HTTPBasicAuth
import base64
import json
import keys

# get Oauth token from M-pesa [function]
def get_mpesa_token():

    consumer_key = "lyLg2cLJBFKnPSSO0Dz544GNrKGUJ8eN"
    consumer_secret = "7AcH6LlYBAMQ5hIt"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    # make a get request using python requests liblary
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # return access_token from response
    return r.json()['access_token']
 
access_token = get_mpesa_token()
headers = {
  'Content-Type': 'application/json',
  'Authorization': f"Bearer {access_token}"
}

def lipa_na_mpesa():
    payload = {
        "BusinessShortCode": keys.BusinessShortCode,
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwNjI5MDk0NzUz",
        "Timestamp": "20230629094753",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": keys.PhoneNumber,
        "PartyB": keys.BusinessShortCode,
        "PhoneNumber": keys.PhoneNumber,
        "CallBackURL": "https://denvic.co.ke.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X" 
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)
    print(response.text.encode('utf8'))

lipa_na_mpesa()