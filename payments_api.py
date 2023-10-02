import requests
import json
from application import data as config


api_key="DRiJU547bgKP50DlsesEHRXawLw4mP7ymO1Ow48bYuw"
cc_key="c92edadf-6e68-4e9e-b9e1-90813db1f043"
cb_url="https://api.commerce.coinbase.com/charges"
headers = {
    "accept":"application/json",
    "content_type":"application/json",
    "X-CC-Api-Key": cc_key,
    "X-CC-Version": "2018-03-22"
}

def handle_paypal_payment(amount, currency, return_url, cancel_url):
    paypalrestsdk.configure({
        "mode": "sandbox", 
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET"
    })
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": return_url,
            "cancel_url": cancel_url
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": amount,
                    "currency": currency,
                    "quantity": 1
                }]
            },
            "amount": {
                "total": amount,
                "currency": currency
            },
            "description": "This is the payment description."
        }]
    })
    if payment.create():
        print("Payment created successfully")
    else:
        print(payment.error)

def handle_stripe_payment(amount, currency, description, source):
    stripe.api_key = "YOUR_API_KEY"
    charge = stripe.Charge.create(
        amount=amount,
        currency=currency,
        description=description,
        source=source,
    )
    return charge
def handle_coinbase_payment(amount, currency, description, redirect_url, cancel_url):
    data={
        "name": description,
        "description": description,
        "pricing_type":"fixed_price",
        "local_price": {
            "amount": amount,
            "currency": currency
        },
        "metadata": {
            "customer_id": "id_1005",
            "customer_name": "Satoshi Nakamoto"
        },
        "redirect_url": redirect_url,
        "cancel_url": cancel_url
    }
    res = requests.post(cb_url, data=json.dumps(data), headers=headers)
    if res.status_code == 201:
        response_dict = json.loads(res.text)
        return response_dict["data"]["hosted_url"]
    else:
        return False


def create_deposit_charge(chat_id):
    data={
        "name":"Deposit",
        "description": f"Deposit-{chat_id}",
        "pricing_type":"no_price",
        "redirect_url": config.redirect_url,
        "cancel_url": config.cancel_url
    }
    res = requests.post(cb_url, data=data, headers=headers)
    print("f")
    if res.status_code == 401:
        return False
    else:
        response_dict = json.loads(res.text)
        return response_dict["data"]["hosted_url"]

