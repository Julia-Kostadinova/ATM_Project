
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
