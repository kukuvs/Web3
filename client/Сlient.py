import requests
import json

class Client:
    def __init__(self, server_url):
        self.server_url = server_url
    
    def encrypt_data(self, data, key):
        response = requests.post(f"{self.server_url}/encrypt", json={'data': data, 'key': key})
        return response.json()
    
    def decrypt_data(self, encrypted_data, key):
        response = requests.post(f"{self.server_url}/decrypt", json={'encrypted_data': encrypted_data, 'key': key})
        return response.json()

if __name__ == "__main__":
    client = Client(server_url="http://127.0.0.1:5000")
    
    key = "ключ из флешки"
    data = "Пример данных"
    
    # Шифрование данных
    encrypted_response = client.encrypt_data(data, key)
    print("Зашифрованные данные:", encrypted_response)
    
    # Дешифрование данных
    encrypted_data = encrypted_response.get('encrypted_data')
    decrypted_response = client.decrypt_data(encrypted_data, key)
    print("Дешифрованные данные:", decrypted_response)
