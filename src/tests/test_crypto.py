import pytest
from cryptography.fernet import Fernet
from ..Crypto import Crypto

@pytest.fixture
def crypto():
    """
    Фикстура для инициализации объекта Crypto перед каждым тестом.
    """
    return Crypto()

def test_encryption_and_decryption(crypto):
    """
    Тест на шифрование и дешифровку данных.
    """
    key = Fernet.generate_key().decode('utf-8')
    crypto.set_key(key)
    
    data = "Тестовые данные"
    encrypted_data = crypto.incrypt(data)
    
    assert encrypted_data is not None, "Шифрование не удалось"
    
    decrypted_data = crypto.decrypt(encrypted_data)
    
    assert decrypted_data == data, "Дешифровка вернула неверные данные"
