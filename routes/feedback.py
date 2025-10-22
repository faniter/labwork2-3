from flask import Blueprint, render_template, request, redirect, url_for
from models import get_db_conn

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['GET', 'POST'])
def handle_feedback():
    # Якщо користувач надсилає форму (метод POST)
    if request.method == 'POST':
        # 1. Отримуємо дані з форми
        user_name = request.form['user_name']
        email = request.form['email']
        message = request.form['message']
        
        # 2. Зберігаємо дані в БД
        conn = get_db_conn()
        conn.execute(
            'INSERT INTO feedback (user_name, email, message) VALUES (?, ?, ?)',
            (user_name, email, message)
        )
        conn.commit()
        conn.close()
        
        # 3. Перенаправляємо користувача назад на головну
        return redirect(url_for('shop.home'))

    # Якщо користувач просто відкриває сторінку (метод GET)
    # показуємо йому HTML-форму
    return render_template('feedback.html')