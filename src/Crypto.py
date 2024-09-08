
from cryptography.fernet import Fernet

class Crypto:
    """
    Класс Crypto для шифрования и дешифровки данных с использованием Fernet.
    """
    def __init__(self):
        self.key = None
        self.Value = None
        self.encryptedValue = None

    def set_key(self, key):
        """
        Устанавливает ключ для шифрования и дешифровки.
        """
        if not key:
            raise ValueError("Ключ не может быть пустым")
        self.key = key

    def incrypt(self, value):
        """
        Шифрует данные с использованием ключа.
        """
        if not self.key:
            raise ValueError("Ключ не установлен")
        self.Value = value
        self.encryptedValue = Fernet(self.key).encrypt(self.Value.encode('utf-8'))
        return self.encryptedValue

    def decrypt(self, encrypted_value):
        """
        Дешифрует данные с использованием ключа.
        """
        if not self.key:
            raise ValueError("Ключ не установлен")
        self.encryptedValue = encrypted_value
        self.Value = Fernet(self.key).decrypt(self.encryptedValue).decode('utf-8')
        return self.Value

    def clear_key(self):
        """
        Очищает ключ из памяти после использования.
        """
        self.key = None
