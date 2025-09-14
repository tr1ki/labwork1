import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            color TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET'])
def index():
    with open('index.html', encoding='utf-8') as f:
        html = f.read()
    return render_template_string(html)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    color = request.form.get('color')
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute('INSERT INTO submissions (name, email, color) VALUES (?, ?, ?)', (name, email, color))
    conn.commit()
    conn.close()
    return "Данные сохранены"

if __name__ == '__main__':
    app.run(debug=True)