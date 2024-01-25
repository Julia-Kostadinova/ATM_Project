print('***** PYTHON BANK *****')

# main_new.py
from ATM_functions.display_main_menu import display_main_menu, get_user_input
from ATM_functions.display_enterance_client import display_enterance_clients
from ATM_functions.DB import DB

def main():
    display_main_menu()
    user_choice_main_menu = get_user_input()
    display_enterance_clients(user_choice_main_menu)


    
    

if __name__ == "__main__":
    main()

