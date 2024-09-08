import pytest
from ..Parser import Parser

@pytest.fixture
def parser():
    """
    Фикстура для инициализации объекта Parser перед каждым тестом.
    """
    return Parser()

def test_parse_valid_json(parser):
    """
    Тест на успешный парсинг корректного JSON.
    """
    json_data = '{"value": "Тестовые данные"}'
    parsed_value = parser.parse(json_data)
    
    assert parsed_value == "Тестовые данные", "Парсинг вернул неверное значение"

def test_parse_invalid_json(parser):
    """
    Тест на обработку некорректного JSON.
    """
    with pytest.raises(ValueError):
        parser.parse('некорректные данные')
