async def user_registration(user_id):
    with open ('users_data.env' , 'r') as file:
        user_list = file.readlines()
    if user_id in user_list:
        return 'You are already registrated'
    else:
        if user_list == []:
            with open('users_data.env', 'w') as file:
                file.write(user_id)
        else:
            with open('users_data.env', 'a') as file:
                file.writelines(f'\n{user_id}')
        return 'Success! Your id has been registrated'      
    

