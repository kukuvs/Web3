from flask import Flask, request, jsonify
from Crypto import Crypto

def create_app():
    app = Flask(__name__)
    crypto = Crypto()

    @app.route('/encrypt', methods=['POST'])
    def encrypt_data():
        try:
            data = request.json.get('data')
            key = request.json.get('key')
            crypto.set_key(key)
            encrypted_data = crypto.incrypt(data)
            return jsonify({'encrypted_data': encrypted_data}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/decrypt', methods=['POST'])
    def decrypt_data():
        try:
            encrypted_data = request.json.get('encrypted_data')
            key = request.json.get('key')
            crypto.set_key(key)
            decrypted_data = crypto.decrypt(encrypted_data)
            return jsonify({'decrypted_data': decrypted_data}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
