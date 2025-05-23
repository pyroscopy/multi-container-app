from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

# 데이터베이스 연결 설정
db_config = {
    'host': os.getenv('DB_HOST', 'db'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'testdb')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM messages')
        messages = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', messages=messages)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 