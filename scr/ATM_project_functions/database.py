
import json
import os
from ATM_project_functions.account_operations import Clients

class DB:
    @staticmethod
    def load_clients_from_db(file_path='C:/Users/djuli/OneDrive/Desktop/Lekcii Python 1508/Python_Projects/ATM_Project/DB/clients_accounts.json'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                clients_data = json.load(file)
                clients = [Clients(**client_data) for client_data in clients_data]
            return clients
        except FileNotFoundError:
            print(f"Грешка: Файлът '{file_path}' не е намерен.")
            return []
