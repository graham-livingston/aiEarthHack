import csv
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'row_index' not in session:
        session['row_index'] = 0

    with open('cleandata.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if request.method == 'POST':
        session['row_index'] += 1

    row = rows[session['row_index']]
    return render_template('index.html', column2=row[1], column3=row[2], text=session.get('text'))

@app.route('/text', methods=['POST'])
def text():
    session['text'] = request.form.get('text')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
