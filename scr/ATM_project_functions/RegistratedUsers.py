from ATM_project_functions.client_interface_messages import display_main_menu, get_user_input, get_user_input_operation
from ATM_project_functions.account_operations import AccountOperations
from ATM_project_functions.Clients import Clients
from ATM_project_functions.database import DB
from ATM_project_functions.RegistratedUsers import RegistratedUsers





class RegistratedUsers:
 
 def __init__ (self,user_input,client_id,identified_client):
    self.user_input= user_input
    self.client_id=client_id
    self.identified_client=identified_client

if user_input == 1: 
        client_id = input("Моля, въведете своя уникален ID код: ")
        identified_client = identify_client_by_id(client_id)

          
    #pin_code_input = input("Моля, въведете своя ПИН код: ")

    
#if pin_code_input == identified_client.pin_code:
 #       print("ПИН кодът е валиден.")

        if identified_client:
            print(f"Добре дошли, {identified_client.name}!")  
            print("Моля, изберете опция: \n 1. Теглене  \n 2. Внасяне \n 3. Баланс")
    
            user_choice_operation = get_user_input_operation()
            
            if user_choice_operation == 1:
                amount = float(input("Моля, въведете сумата за теглене: "))
                AccountOperations.withdraw(identified_client, amount)
            elif user_choice_operation == 2:
                amount = float(input("Моля, въведете сумата за внасяне: "))
                AccountOperations.deposit(identified_client, amount)
            elif user_choice_operation == 3:
                balance = AccountOperations.check_balance(identified_client)
                print(f"Текущ баланс: {balance}")
            else:
                print("Невалиден избор за операция.")
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
