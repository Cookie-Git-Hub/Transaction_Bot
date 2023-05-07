import requests
import time

url = "https://api.bscscan.com/api"
with open('functions/bsc_scan/bsc_api.env', 'r') as file:
    api_key = file.read()

def create_address_list():
    with open('functions/bsc_scan/bsc_address_list.txt', 'r') as file:
        address_list = file.readlines()
    address_list = [address.strip() for address in address_list]
    return address_list

def add_address_to_list(address):
    address_list = create_address_list()
    if address not in address_list:
        with open('functions/bsc_scan/bsc_address_list.txt', 'a') as file:
            file.write("\n" + address)
        return "Address added"
    else:
        return "Address is already in list"

def remove_address_from_list(address):
    address_list = create_address_list()
    if address in address_list:
        address_list.remove(address)
        with open('functions/bsc_scan/bsc_address_list.txt', 'w') as file:
            for address in address_list:
                if address_list.index(address) != (len(address_list)-1):
                    file.writelines(address + "\n")
                else:
                    file.writelines(address)
        return "Address has been removed"
    else:
        return "No such address in list"

def bsc_checker():
    messages = []
    address_list=create_address_list()
    for addresses in address_list:
        parameters = {
            "module": "account",
            "action": "tokentx",
            "address": addresses,
            "page": "1",
            "offset": "30",
            "startblock": "0",
            "endblock": "999999999",
            "sort": "desc",
            "apikey": api_key 
        }

        response = requests.get(url, params=parameters)
        if response.status_code == 200:
            data = response.json()
            for tx in data["result"]:
                last_check_time = int(tx["timeStamp"])
                if time.time()-last_check_time<=60:                                                                    
                    from_address = tx["from"]
                    to_address = tx["to"]
                    tx_hash = tx["hash"]
                    value = tx["value"]
                    value = int(value) / 10**18
                    token = tx["tokenSymbol"]
                    message = (f"```\n--------------------------\nFound new transaction:\n--------------------------\nFrom: {from_address}\nTo: {to_address}\nTxHash: {tx_hash}\nAmount: {value} {token}\n```")
                    messages.append(message)
        else:
            return("Error: " + response.text)
    return messages