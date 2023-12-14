
class Clients:
    clients_list = []
    last_assigned_id = 0

    def __init__(self, name, pin_code=None, balance=0, client_id=None):
        if client_id is None:
            Clients.last_assigned_id += 1
            self.client_id = f"{Clients.last_assigned_id:04d}"
        else:
            self.client_id = client_id

        self.name = name
        self.pin_code = pin_code if pin_code is not None else "default_pin"
        self.balance = balance

    def __str__(self):
        return f"Клиент {self.name} (ID: {self.client_id}), Баланс: {self.balance}"

    @classmethod
    def add_client(cls, new_client):
        cls.clients_list.append(new_client)

