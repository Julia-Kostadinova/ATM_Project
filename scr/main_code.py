
print('***** PYTHON BANK *****')

from ATM_project_functions.client_interface_messages import display_main_menu, get_user_input,get_user_input_operation
from ATM_project_functions.account_operations import AccountOperations
from ATM_project_functions.database import DB

def identify_client_by_id(client_id):
    try:
        clients_list = DB.load_clients_from_db()
        for client in clients_list:
            if client.client_id == client_id:
                return client
        return None
    except Exception as e:
        print(f"An error occurred while loading clients: {e}")
        return None

def main():
    display_main_menu()
    user_choice = get_user_input()

    if user_choice == 1: 
        client_id = input("Моля, въведете своя уникален ID код: ")
        identified_client = identify_client_by_id(client_id)

        if identified_client:
            print(f"Добре дошли, {identified_client.name}!")  
            print("Моля, изберете опция: \n 1. Теглене  \n 2. Внасяне \n 3. Баланс")
    
            get_user_input_operation()
            user_choice_operation = get_user_input_operation()
            

        else:
            print("Невалиден ID код. Моля, опитайте отново или регистрирайте нов акаунт.")

    elif user_choice == 2: 
        new_client_name = input("Моля, въведете вашето име: ")
        new_client_pin_code = input("Моля, въведете ПИН код: ")
        new_client = Clients(new_client_name, new_client_pin_code)
        Clients.add_client(new_client)
        print(f"Регистрацията е успешна, {new_client.name}! Добре дошли в нашата банка.\n Ще получите SMS с Вашия уникален ID код.")             

    else:
        print("Невалиден избор. Програмата ще приключи.")


  

if __name__ == "__main__":
    main()
