from .Crypto import Crypto
from .Parser import Parser
import os

class Main:
    """
    Главный класс для обработки данных и взаимодействия с флеш-накопителем.
    """
    def __init__(self):
        self.crypto = Crypto()
        self.parser = Parser()

    def check_usb_key(self):
        """
        Проверяет наличие флеш-накопителя с ключом.
        """
        usb_path = "/mnt/usb/key.txt"  # Путь к флешке с ключом
        if os.path.exists(usb_path):
            return usb_path
        else:
            raise Exception("Флеш-накопитель с ключом не подключён!")

    def get_key_from_usb(self):
        """
        Считывает ключ с флешки.
        """
        usb_path = self.check_usb_key()
        with open(usb_path, 'r') as f:
            return f.read().strip()

    def process_data(self, json_data):
        """
        Основной процесс обработки данных: парсинг, шифрование и дешифровка.
        """
        try:
            # Считываем и устанавливаем ключ с флешки
            key = self.get_key_from_usb()
            self.crypto.set_key(key)

            # Парсинг данных
            value = self.parser.parse(json_data)

            # Шифрование данных
            encrypted_data = self.crypto.incrypt(value)
            print(f"Зашифрованные данные: {encrypted_data}")

            # Дешифрование данных
            decrypted_data = self.crypto.decrypt(encrypted_data)
            print(f"Дешифрованные данные: {decrypted_data}")

            return decrypted_data
        finally:
            # Очищаем ключ после работы для безопасности
            self.crypto.clear_key()

if __name__ == "__main__":
    main = Main()
    
    # Тестовые данные в формате JSON
    json_data = '{"value": "Тестовые данные"}'
    print("Обработанные данные:", main.process_data(json_data))
