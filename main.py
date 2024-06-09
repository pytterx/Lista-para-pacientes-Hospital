from flask import Flask, render_template, redirect, url_for, request
from bc import sqlite3

app = Flask(__name__)

def conectar_bd():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = conectar_bd()
    if request.method == 'POST':
        name = request.form['name']
        sintoma = request.form['sintoma']
        numero = request.form['numero']
        data_de_naicimento = request.form['data_de_naicimento']        
        conn.execute('INSERT INTO data(name, sintoma, numero, data_de_naicimento) VALUES (? , ?,  ?, ?)', (name, sintoma, numero, data_de_naicimento ))

        conn.commit()
        return redirect(url_for('index'))
        
    name = conn.execute('SELECT * FROM data').fetchall()
    conn.close()
    return render_template('index.html', data_list=name)



if __name__ == '__main__':
    app.run(debug=True)