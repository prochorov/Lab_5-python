import random
import string


def generate_random_filename(length, extension):
    # Генерируем случайную строку из символов английского алфавита в разных регистрах
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    # Добавляем расширение
    return f'{random_string}.{extension}'


# Пример использования:
filename = generate_random_filename(8, 'txt')
print(filename)
