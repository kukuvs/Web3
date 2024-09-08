import pytest
from ..server import create_app  # Корректируем импорт

@pytest.fixture
def app():
    """Фикстура для создания Flask приложения для тестов."""
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Фикстура для создания тестового клиента."""
    return app.test_client()

def test_server_status(client):
    """Тест на проверку статуса сервера."""
    response = client.get('/')
    assert response.status_code == 404  # Убедимся, что маршрут '/' не существует

def test_encrypt(client):
    """Тест на проверку маршрута шифрования."""
    data = {'data': 'Тестовые данные', 'key': 'секретный_ключ'}
    response = client.post('/encrypt', json=data)
    assert response.status_code == 200
    assert 'encrypted_data' in response.json

def test_decrypt(client):
    """Тест на проверку маршрута дешифрования."""
    encrypted_data = {'encrypted_data': '...', 'key': 'секретный_ключ'}  # Заменить зашифрованные данные на валидные
    response = client.post('/decrypt', json=encrypted_data)
    assert response.status_code == 200
    assert 'decrypted_data' in response.json
