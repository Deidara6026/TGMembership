import requests
import json
from application import data as config


api_key="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
cc_key="kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
cb_url="https://api.commerce.coinbase.com/charges"
headers = {
    "accept":"application/json",
    "content_type":"application/json",
    "X-CC-Api-Key": cc_key,
    "X-CC-Version": "2018-03-22"
}



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

