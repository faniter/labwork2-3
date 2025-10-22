from flask import Flask
# Імпортуємо нашу функцію ініціалізації БД з файлу models.py
from models import init_db

# Імпортуємо наші "креслення" (blueprints) з папки routes
from routes.shop import shop_bp
from routes.admin import admin_bp
from routes.feedback import feedback_bp

# 1. Запускаємо функцію ініціалізації
# Вона перевірить, чи існує файл db.sqlite, і якщо ні - 
# створить його та всі потрібні таблиці (sneakers, feedback)
init_db()

# 2. Створюємо сам додаток Flask
app = Flask(__name__)

# 3. ДОДАНО: Секретний ключ для сесій (кошика)
# Змініть це на будь-який випадковий набір символів!
app.config['SECRET_KEY'] = 'your-very-secret-random-key-12345' 

# 4. Реєструємо наші маршрути (сторінки)
app.register_blueprint(shop_bp) 
app.register_blueprint(admin_bp, url_prefix='/admin') 
app.register_blueprint(feedback_bp) 

# 5. Запускаємо додаток
if __name__ == '__main__':
    app.run(debug=True)