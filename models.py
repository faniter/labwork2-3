import sqlite3
import os

# Назва нашої бази даних
DB_NAME = 'db.sqlite'

def get_db_conn():
    """Створює з'єднання з базою даних."""
    # os.path.dirname(__file__) - це шлях до поточної папки
    # os.path.join з'єднує шлях до папки та назву файлу
    db_path = os.path.join(os.path.dirname(__file__), DB_NAME)
    
    # Створюємо з'єднання
    conn = sqlite3.connect(db_path)
    
    # Це налаштування дозволить нам отримувати дані як словники (dict)
    # (наприклад: row['name']), а не кортежі (tuple) (row[1])
    # Це набагато зручніше для HTML-шаблонів
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Ініціалізує базу даних. 
    Створює файл db.sqlite, якщо його немає, 
    та додає таблиці 'sneakers' і 'feedback'.
    """
    # Перевіряємо, чи існує файл БД
    db_path = os.path.join(os.path.dirname(__file__), DB_NAME)
    db_created = not os.path.exists(db_path)
    
    # Створюємо з'єднання (це автоматично створить файл, якщо його немає)
    conn = get_db_conn()
    cursor = conn.cursor() # Створюємо курсор
    
    # Створюємо таблицю 'sneakers', ЯКЩО ВОНА ЩЕ НЕ ІСНУЄ
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sneakers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image_url TEXT
    )
    ''')
    
    # Створюємо таблицю 'feedback', ЯКЩО ВОНА ЩЕ НЕ ІСНУЄ
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Зберігаємо зміни
    conn.commit()
    conn.close()
    
    if db_created:
        print(f"Базу даних {DB_NAME} та таблиці успішно створено.")
    else:
        # Ми запускаємо це кожного разу, 
        # 'CREATE TABLE IF NOT EXISTS' захистить від помилок
        print("База даних вже існує. Таблиці перевірено.")