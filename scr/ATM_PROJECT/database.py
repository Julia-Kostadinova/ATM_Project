
import json
import os
from ATM_project.account_operations import Clients

class DB:
    @staticmethod
    def load_clients_from_db(file_path='C:/Users/djuli/OneDrive/Desktop/Lekcii Python 1508/Python_Projects/ATM_Project/DB/clients_accounts.json'):
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if not os.path.exists(file_path):
            # Create an empty file if it doesn't exist
            with open(file_path, 'w') as file:
                json.dump([], file)
        try:
            with open(file_path, 'r') as file:
                clients_data = json.load(file)
                clients = [Clients(**client_data) for client_data in clients_data]
            return clients
        except FileNotFoundError:
            print(f"Грешка: Файлът '{file_path}' не е намерен.")
            return []
