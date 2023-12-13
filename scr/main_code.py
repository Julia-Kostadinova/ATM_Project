
print('***** PYTHON BANK *****')

from ATM_project_functions.client_interface_messages import display_main_menu, get_user_input
from ATM_project_functions.account_operations import Clients
from ATM_project_functions.account_operations import AccountOperations
from ATM_project_functions.database import DB

def identify_client_by_id(client_id):
    clients_list = DB.load_clients_from_db()
    for client in clients_list:
        if client.client_id == client_id:
           return client
    return None

def main():
    display_main_menu()
    user_choice = get_user_input()

    if user_choice == 1: 
        client_id = input("Моля, въведете своя уникален ID код: ")
        identified_client = identify_client_by_id(client_id)

        if identified_client:
            print(f"Добре дошли, {identified_client.name}!")
            
        else:
            print("Невалиден ID код. Моля, опитайте отново или регистрирайте нов акаунт.")

    elif user_choice == 2: 
        new_client_id = input("Моля, въведете нов уникален ID код за вашия акаунт: ")
        new_client_name = input("Моля, въведете вашето име: ")
        new_client_pin_code = input("Моля, въведете ПИН код: ")
        new_client_balance = 0

        new_client = Clients(new_client_id,new_client_name, new_client_pin_code,new_client_balance) 
        Clients.add_client(new_client)
        print(f"Регистрацията е успешна, {new_client.name}! Добре дошли в нашата банка.")
        
    else:
        print("Невалиден избор. Програмата ще приключи.")

if __name__ == "__main__":
    main()
