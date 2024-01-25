class Clients:
 
    def __init__(self, name, pin_code, balance):
        self.name = name
        self.pin_code = pin_code 
        self.balance = balance

    def __str__(self):
        return f"Клиент {self.name} (ID: {self.client_id}), Баланс: {self.balance}"
