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

# 3. Реєструємо наші маршрути (сторінки)
# Це каже Flask: "Візьми всі маршрути з файлу routes/shop.py"
app.register_blueprint(shop_bp) 

# Це каже Flask: "Візьми всі маршрути з routes/admin.py
# і зроби так, щоб вони починалися з /admin"
app.register_blueprint(admin_bp, url_prefix='/admin') 

# Це каже Flask: "Візьми всі маршрути з routes/feedback.py"
app.register_blueprint(feedback_bp) 

# 4. Запускаємо додаток, якщо цей файл запустили напряму
if __name__ == '__main__':
    app.run(debug=True)