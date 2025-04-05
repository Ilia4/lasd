from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr  # Получаем IP-адрес пользователя
    print(f"IP-адрес пользователя: {user_ip}")
    return f"Ваш IP-адрес: {user_ip}"

if __name__ == '__main__':
    # Используем переменную окружения PORT, чтобы приложение работало на правильном порту
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)