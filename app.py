from flask import Flask, render_template
# 1. Імпортуємо SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 2. Налаштовуємо базу даних
# Вказуємо, що наша БД буде називатись 'shop.db' і лежатиме в тій самій папці
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

# 3. Створюємо "Модель" (опис таблиці)
# Це наш "креслення" для кросівок
class Sneaker(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Унікальний ID
    name = db.Column(db.String(100), nullable=False) # Назва
    description = db.Column(db.Text, nullable=True) # Опис
    price = db.Column(db.Integer, nullable=False) # Ціна
    image_url = db.Column(db.String(200), nullable=True) # Посилання на фото

    def __repr__(self):
        return f'<Sneaker {self.name}>'

# 4. Оновлюємо маршрут (route), щоб він брав дані з БД
@app.route('/')
def home():
    # Замість простого рендерингу, ми спочатку
    # просимо у БД *всі* кросівки, які в ній є
    all_sneakers = Sneaker.query.all()
    
    # Потім передаємо цей список у наш шаблон
    return render_template('home.html', sneakers=all_sneakers)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)