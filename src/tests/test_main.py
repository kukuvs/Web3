import pytest
from unittest.mock import patch
import sys
import os
from cryptography.fernet import Fernet

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.Main import Main

@pytest.fixture
def main():
    """
    Фикстура для инициализации объекта Main перед каждым тестом.
    """
    return Main()

# Генерация корректного base64 ключа для шифрования
valid_key = Fernet.generate_key()

@patch('src.Main.Main.get_key_from_usb', return_value=valid_key.decode('utf-8'))  # Используем корректный base64 ключ
def test_process_data(mock_get_key_from_usb, main):
    """
    Тест на обработку данных с корректным ключом.
    """
    json_data = '{"value": "Тестовые данные"}'
    processed_data = main.process_data(json_data)
    
    assert processed_data == "Тестовые данные", "Обработанные данные не совпадают с исходными"
