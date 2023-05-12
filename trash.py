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