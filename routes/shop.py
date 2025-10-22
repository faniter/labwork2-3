from flask import Blueprint, render_template
from models import get_db_conn

shop_bp = Blueprint('shop', __name__)

@shop_bp.route('/')
def home():
    conn = get_db_conn()
    # Отримуємо всі кросівки з БД
    sneakers_rows = conn.execute('SELECT * FROM sneakers').fetchall()
    conn.close()
    
    # Передаємо список у шаблон home.html
    return render_template('home.html', sneakers=sneakers_rows)

@shop_bp.route('/about')
def about():
    return render_template('about.html')