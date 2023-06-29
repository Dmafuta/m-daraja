import requests
import keys

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer WLnByHwRLgKwVLILJD0m4Bm0UQoy'

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