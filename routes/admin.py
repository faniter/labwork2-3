from flask import Blueprint, render_template, request, redirect, url_for
from models import get_db_conn

admin_bp = Blueprint('admin', __name__)

# --- Відгуки (Feedback) ---

@admin_bp.route('/admin')
def admin_dashboard():
    conn = get_db_conn()
    feedbacks = conn.execute('SELECT * FROM feedback ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('admin.html', feedbacks=feedbacks)

@admin_bp.route('/admin/delete_feedback/<int:feedback_id>', methods=['POST'])
def delete_feedback(feedback_id):
    conn = get_db_conn()
    conn.execute('DELETE FROM feedback WHERE id = ?', (feedback_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin.admin_dashboard'))

# --- НОВИЙ КОД: Керування Категоріями ---

@admin_bp.route('/admin/categories', methods=['GET', 'POST'])
def manage_categories():
    conn = get_db_conn()
    
    if request.method == 'POST':
        # Якщо форма додавання була надіслана
        if request.form['action'] == 'add':
            category_name = request.form['name']
            if category_name:
                try:
                    conn.execute('INSERT INTO categories (name) VALUES (?)', (category_name,))
                    conn.commit()
                except conn.IntegrityError:
                    # Якщо категорія вже існує (через UNIQUE)
                    pass 
        return redirect(url_for('admin.manage_categories'))

    # (GET) Просто показуємо сторінку
    categories = conn.execute('SELECT * FROM categories ORDER BY name').fetchall()
    conn.close()
    return render_template('admin_categories.html', categories=categories)

@admin_bp.route('/admin/delete_category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    conn = get_db_conn()
    try:
        # Видаляємо категорію
        conn.execute('DELETE FROM categories WHERE id = ?', (category_id,))
        conn.commit()
    except conn.IntegrityError:
        # Помилка: Не можна видалити категорію, доки до неї прив'язані товари
        # (Це добре, це захист FOREIGN KEY)
        # TODO: Додати повідомлення про помилку
        pass
    conn.close()
    return redirect(url_for('admin.manage_categories'))