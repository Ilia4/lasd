from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем реальный IP-адрес пользователя из заголовков
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"IP-адрес пользователя: {user_ip}")
    return f"Ваш IP-адрес: {user_ip}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Используем переменную окружения для порта
    app.run(host="0.0.0.0", port=port, debug=True)
