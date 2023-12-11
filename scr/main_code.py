
print( '***** PYTHON BANK *****')


from ATM_PROJECT import client_interface_messages

def main():
    client_interface_messages.display_main_menu()
    client_interface_messages.get_user_input()



if __name__ == "__main__":
    main()