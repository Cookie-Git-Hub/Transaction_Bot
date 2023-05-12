def show_address_list():
    message = f'**Your address list:**\n'
    address_list = []
    with open (f'address_list.txt', 'r') as file:
        address_list = file.readlines()   
    for address in address_list:
        message = f'{message}{address}'
    if message == '**Your address list:**':
        return 'Your address list is empty'
    return message