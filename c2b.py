import requests

def register_url():
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer dqZSuNgCrHsZuA8hF7G8grJ97VIB'
    }

    payload = {
        "ShortCode": 600988,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://denvic.co.ke/confirmation",
        "ValidationURL": "https://denvic.co.ke/validation",
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers = headers, json = payload)
    print(response.text.encode('utf8'))


register_url()