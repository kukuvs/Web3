import pytest
import requests_mock
from ..Сlient import Client  # Импорт клиента

@pytest.fixture
def client():
    """
    Фикстура для создания клиента.
    """
    return Client()  # Создаём экземпляр клиента

def test_client_get_data(client):
    """
    Тест на проверку получения данных через клиента.
    """
    with requests_mock.Mocker() as m:
        # Мокируем ответ сервера на запрос
        m.get('http://localhost:5000/data', json={'data': 'Тестовые данные'})
        
        # Вызываем метод клиента для получения данных
        data = client.get_data()
        
        # Проверяем, что клиент получил данные правильно
        assert data == 'Тестовые данные'

def test_client_post_data(client):
    """
    Тест на проверку отправки данных через клиента.
    """
    with requests_mock.Mocker() as m:
        # Мокируем ответ сервера на POST запрос
        m.post('http://localhost:5000/data', json={'status': 'success'})
        
        # Вызываем метод клиента для отправки данных
        status = client.post_data('Тестовые данные')
        
        # Проверяем, что сервер вернул успех
        assert status == 'success'
