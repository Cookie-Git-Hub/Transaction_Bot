import requests
import time

api_keys = {'bscscan': 'T19C2IRN7X8MPAW9TJVHXK7ANHJ487FHG3','etherscan': 'HVTN6MSTWF2PZP9HFZV9H1VVS33ENQYJXK', 'polygon': 'F8VFVSTRFDNUZSC3EPMT4WZ76FCFE2YG16', 'optimistic_etherscan': 'XQS315ITEVZD5S2CUDJQ28VI8Y1DBZUYRX'}
url = {'bscscan':'https://api.bscscan.com/api', 'etherscan':'https://api.etherscan.io/api', 'polygon':'https://api.polygonscan.com/api', 'optimistic_etherscan':'https://api-optimistic.etherscan.io/api'}
coin = {'bscscan':'BNB', 'etherscan':'ETHER', 'polygon':'MATIC', 'optimistic_etherscan':'ETHER'}

def add_address_to_list(address):
    filename = f'address_list.txt'
    with open (filename, 'a') as file:
        file.close()
    with open (filename, 'r') as file:
        address_list = file.readlines()
        address_list = [address.strip() for address in address_list]
        if address not in address_list:
            with open(filename, 'a') as file:
                if address_list == []:
                    file.write(address)
                else:
                    file.write("\n" + address)
            return "Address added"
        else:
            return "Address is already in list"
        

def remove_address_from_list(address):
    filename = f'address_list.txt'
    with open (filename, 'a') as file:
        file.close()     
    with open (filename, 'r') as file:
        address_list = file.readlines()
        address_list = [address.strip() for address in address_list]
        if address in address_list:
            address_list.remove(address)
            with open(filename, 'w') as file:
                for address in address_list:
                    if address_list.index(address) != (len(address_list)-1):
                        file.writelines(address + '\n')
                    else:
                        file.writelines(address)
            return "Address has been removed"
        else:
            return "Address is not in list"  


def coin_checker():
    messages = []
    for site in url:
        try:
            filename = f'address_list.txt'  
            with open (filename, 'r') as file:
                address_list = file.readlines()
                address_list = [address.strip() for address in address_list]
            if site != 'bscscan':
                offset = '4'
            else:
                offset = '2'
            for addresses in address_list:
                parameters = {
                    "module": "account",
                    "action": "tokentx",
                    "address": addresses,
                    "page": "1",
                    "offset": offset,
                    "startblock": "0",
                    "endblock": "999999999",
                    "sort": "desc",
                    "apikey": api_keys[site] 
                }

            response = requests.get(url[site], params=parameters)
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
                        value = ('{:.4f}'.format(value))
                        token = tx["tokenSymbol"]
                        message = (f"\n--------------------------\n**Found new transaction on {site}:**\n--------------------------\n**From:** {from_address}\n**To:** {to_address}\n**TxHash:** {tx_hash}\n**Amount:** {value} **{token}**\n")
                        messages.append(message)
            else:
                return("Error: " + response.text)
        except:
            pass
    return messages

def transaction_checker():
    messages = []
    for site in url:
        try:
            filename = f'address_list.txt' 
            with open (filename, 'r') as file:
                address_list = file.readlines()
                address_list = [address.strip() for address in address_list]
            for addresses in address_list:
                parameters = {
                    "module": "account",
                    "action": "txlist",
                    "address": addresses,
                    "page": "1",
                    "offset": "30",
                    "startblock": "0",
                    "endblock": "999999999",
                    "sort": "desc",
                    "apikey": api_keys[site] 
                }

                response = requests.get(url[site], params=parameters)
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
                            value = ('{:.4f}'.format(value))
                            message = (f"\n--------------------------\n**Found new transaction on {site}:**\n--------------------------\n**From:** {from_address}\n**To:** {to_address}\n**TxHash:** {tx_hash}\n**Amount:** {value} **{coin[site]}**\n")
                            messages.append(message)
                else:
                    return("Error: " + response.text)
        except:
            pass
    return messages