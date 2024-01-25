from ATM_functions import DB

def display_enterance_clients(user_choice_main_menu):
    if user_choice_main_menu == 1:
        client_id = input("Моля, въведете своя уникален ID код: ")
        db = DB()
        db.connect_to_local_cluster()
        identified_client = db.identify_client_by_id(client_id)
        if identified_client:
            print(f"Добре дошли, {identified_client}!")
        else:
            print("Клиент с този ID не съществува.")
    elif user_choice_main_menu == 2:
        new_client_name = input("Моля, въведете вашето име: ")
        while not new_client_name.isalpha():
            print("Невалидно име. Моля, въведете само букви.")
            new_client_name = input("Моля, въведете вашето име: ")
            DB.insert_db_record(new_client_name)
        #new_client_pin_code = int(input("Моля, въведете ПИН код: "))
        print(f"Регистрацията е успешна, {new_client_name}! Добре дошли в нашата банка.\n Ще получите SMS с Вашия уникален ID код.")
    else:
        print("Невалиден избор. Програмата ще приключи.")

       
