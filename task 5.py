import secrets
import string


class Password:
    def __init__(self, *sets):
        # Проверяем, что хотя бы один набор символов был указан
        if not sets:
            raise ValueError('At least one set of characters must be specified')
        # Сохраняем наборы символов в списке
        self.sets = sets

    def generate(self, length):
        # Генерируем пароль
        password = ''
        while len(password) < length:
            # Выбираем случайный набор символов
            set_ = secrets.choice(self.sets)
            # Генерируем случайный символ из этого набора
            char = secrets.choice(set_)
            password += char
        return password


password_generator = Password(string.ascii_lowercase, string.ascii_uppercase, string.digits)
print(password_generator.generate(8))
