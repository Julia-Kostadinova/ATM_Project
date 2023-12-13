

class Clients:
    clients_list = []

    def __init__(self, client_id, name, pin_code, balance):
        self.client_id = client_id
        self.name = name
        self.pin_code = pin_code
        self.balance = balance

    def __str__(self):
        return f"Клиент {self.name} (ID: {self.client_id}), Баланс: {self.balance}"

    @classmethod
    def add_client(cls, new_client):
        cls.clients_list.append(new_client)


class AccountOperations:
    @staticmethod
    def withdraw(client, amount):
        if amount > 0 and client.balance >= amount:
            client.balance -= amount
            return True
        else:
            print("Грешка при теглене. Невалидна сума или недостатъчен баланс.")
            return False

    @staticmethod
    def deposit(client, amount):
        if amount > 0:
            client.balance += amount
            return True
        else:
            print("Грешка при внасяне. Невалидна сума.")
            return False

    @staticmethod
    def check_balance(client):
        return client.balance
