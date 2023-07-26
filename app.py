from flask import Flask, render_template, request, jsonify
import sqlite3
import math
import os
from datetime import datetime

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'calculos.db')


def create_table():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS calculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lado1 REAL,
                lado2 REAL,
                hipotenusa REAL,
                timestamp DATETIME
            )
        ''')


@app.route('/', methods=['GET', 'POST'])
def index():
    create_table()
    if request.method == 'POST':
        lado1 = float(request.form['lado1'])
        lado2 = float(request.form['lado2'])
        hipotenusa = math.sqrt(lado1 ** 2 + lado2 ** 2)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO calculos (lado1, lado2, hipotenusa, timestamp) VALUES (?, ?, ?, ?)',
                           (lado1, lado2, hipotenusa, timestamp))

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT lado1, lado2, hipotenusa, timestamp FROM calculos ORDER BY id DESC')
        history = cursor.fetchall()

    return render_template('index.html', history=history)


if __name__ == '__main__':
    app.run(debug=True)