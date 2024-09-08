import json

class Parser:
    """
    Класс для парсинга и валидации JSON данных.
    """
    def __init__(self):
        self.data = None
        self.Value = None

    def parse(self, json_data):
        """
        Парсит JSON и возвращает значение по ключу 'value'.
        """
        try:
            self.data = json.loads(json_data)
            self.Value = self.data['value']
        except json.JSONDecodeError:
            raise ValueError("Ошибка парсинга JSON")
        except KeyError:
            raise ValueError("Ключ 'value' не найден в JSON")
        return self.Value
