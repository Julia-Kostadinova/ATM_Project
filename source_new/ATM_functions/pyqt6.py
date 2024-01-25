import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        # Създаваме елементи на интерфейса
        self.label_username = QLabel('Потребителско име:')
        self.label_password = QLabel('Парола:')
        self.input_username = QLineEdit()
        self.input_password = QLineEdit()
        self.button_login = QPushButton('Вход')

        # Настройваме полетата за парола да са от тип "парола"
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        # Форматиране на полетата за въвеждане
        self.input_username.setFixedWidth(200)
        self.input_password.setFixedWidth(200)

        # Стилизиране на бутона
        self.button_login.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; }")

        # Създаваме макет за формата
        form_layout = QFormLayout()
        form_layout.addRow(self.label_username, self.input_username)
        form_layout.addRow(self.label_password, self.input_password)

        # Добавяме бутона в хоризонтален макет
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.button_login)

        # Обединяваме формния и бутонния макети в главен вертикален макет
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        # Настойваме макета за главната форма
        self.setLayout(main_layout)

        # Свързваме бутона с функцията за вход
        self.button_login.clicked.connect(self.login)

        # Настройваме размерите и заглавието на прозореца
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('Login Form')

    def login(self):
        # Тук може да добавите логика за проверка на потребителско име и парола
        # За този пример ще използваме просто известни стойности
        username = self.input_username.text()
        password = self.input_password.text()

        if username == 'user' and password == 'pass':
            QMessageBox.information(self, 'Успешен вход', 'Добре дошли, {}'.format(username))
        else:
            QMessageBox.warning(self, 'Грешка', 'Невалидно потребителско име или парола')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Създаваме инстанция на Login формата
    login_form = LoginForm()

    # Показваме формата
    login_form.show()

    # Стартираме приложението
    sys.exit(app.exec())
