from flask import Blueprint, render_template, request, redirect, url_for
from models import get_db_conn

admin_bp = Blueprint('admin', __name__)

# Маршрут для головної сторінки адмінки (показує всі відгуки)
@admin_bp.route('/admin')
def admin_dashboard():
    conn = get_db_conn()
    # Отримуємо всі відгуки з таблиці feedback
    feedbacks = conn.execute('SELECT * FROM feedback ORDER BY created_at DESC').fetchall()
    conn.close()
    
    return render_template('admin.html', feedbacks=feedbacks)

# Маршрут для видалення відгуку
@admin_bp.route('/admin/delete/<int:feedback_id>', methods=['POST'])
def delete_feedback(feedback_id):
    conn = get_db_conn()
    # Виконуємо SQL-запит на видалення за id
    conn.execute('DELETE FROM feedback WHERE id = ?', (feedback_id,))
    conn.commit()
    conn.close()
    
    # Повертаємо користувача назад на сторінку адмінки
    return redirect(url_for('admin.admin_dashboard'))