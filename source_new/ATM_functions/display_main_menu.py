

def display_main_menu():
    display_message=print("Моля, изберете опция: \n 1. Вход  \n 2. Регистрация на нов акаунт")

def get_user_input(prompt="Въведете Вашия избор: "):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in [1, 2]:
                return user_input
            else:
                print("Грешка! Изборът трябва да бъде 1 или 2.")
        except ValueError:
            print("Грешка! Моля, въведете число.")

    

def get_user_input_operation(prompt="Въведете Вашия избор за операция: "):
    while True:
        try:
            user_input_operation = int(input(prompt))
            if user_input_operation in [1,2, 3]:
                return user_input_operation
            else:
                print("Грешка! Изборът трябва да бъде 1,2 или 3.")
        except ValueError:
            print("Грешка! Моля, въведете число.")
