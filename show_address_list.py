def show_address_list(user_id):
    message = '**Your address_list:**'
    sites = ['bscscan', 'etherscan', 'polygon', 'optimistic_etherscan']
    for site in sites:
        address_list = []
        try:
            with open (f'address_lists/{site}/{user_id}_address_list.txt', 'r') as file:
                address_list = file.readlines()
            message = f'  {message}\n**{site}**:'    
            for address in address_list:
                message = f'{message}\n \t{address}'
        except:
            pass
    return message