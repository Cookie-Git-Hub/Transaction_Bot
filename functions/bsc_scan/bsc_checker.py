import requests
import time

url = "https://api.bscscan.com/api"
#with open('bsc_api.env', 'r') as file:
    #api_key = file.read()
#with open('bsc_adress_list.txt', 'r') as file:
    #adress_list = file.read()

parameters = {
    "module": "account",
    "action": "tokentx",
    "contractaddress": "0xc9849e6fdb743d08faee3e34dd2d1bc69ea11a51",
    "address": "0x0BAC492386862aD3dF4B666Bc096b0505BB694Da",  #Нужно заменить на переменную!
    "page": "1",
    "offset": "5",
    "startblock": "0",
    "endblock": "999999999",
    "sort": "asc",
    "apikey": "T19C2IRN7X8MPAW9TJVHXK7ANHJ487FHG3"   #Нужно заменить на переменную!
}

last_tx_count = 0

def bsc_checker():
    while True:
        response = requests.get(url, params=parameters)

        if response.status_code == 200:
            data = response.json()
            tx_count = len(data["result"])
            if tx_count > last_tx_count:
                new_tx_count = tx_count - last_tx_count
                print(f"Found {new_tx_count} new transactions:")
                for i in range(last_tx_count, tx_count):
                    tx = data["result"][i]
                    from_address = tx["from"]
                    to_address = tx["to"]
                    tx_hash = tx["hash"]
                    value = tx["value"]
                    token = tx["tokenSymbol"]
                    print(f"From: {from_address}\nTo: {to_address}\nTxHash: {tx_hash}\nAmount: {value}\nToken: {token}\n")
                last_tx_count = tx_count
        else:
            print("Error: " + response.text)

        time.sleep(30)