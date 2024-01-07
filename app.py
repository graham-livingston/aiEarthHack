import csv
import json

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_session import Session

from itertools import zip_longest

from functions import getResponse, parseResponse

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('appdata'))
    return render_template('index.html')


@app.route('/appdata', methods=['GET', 'POST'])
def appdata():
    
    searchTerm = 'hello'
    if 'row_index' not in session:
        session['row_index'] = 1

    filename = session.get('filename')

    with open(f'{filename}', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if request.method == 'POST':
        session['row_index'] += 1

    row = rows[session['row_index']]
    
    #get response from openai
    resp = parseResponse(getResponse(row[2], searchTerm))
    
    #reading json file for example data
    data = json.loads(resp)
    
    grid = [{'type': 'resource', 'value': val} for val in data['resources']] + [{'type': 'process', 'value': val} for val in data['processes']]
    grid.sort(key=lambda x: x['value']['index'])
    
    return render_template('dashboard.html', column2=row[1], column3=row[2], resp=resp, grid=grid, text=session.get('text'))

@app.route('/text', methods=['POST'])
def text():
    session['text'] = request.form.get('text')
    return redirect(url_for('appdata'))

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(file.filename)
    
    text_inputs = get_text_inputs()
    
    # Store the data in the session
    session['text_inputs'] = text_inputs
    session['filename'] = file.filename

    # Redirect to the appdata route
    return redirect(url_for('appdata'))


def get_text_inputs():
    # Convert the form data to a dictionary
    form_data = request.form.to_dict()

    # Filter out non-text inputs (like the file)
    text_inputs = [value for key, value in form_data.items() if key.startswith('text')]

    return text_inputs

if __name__ == '__main__':
    app.run(debug=True)
