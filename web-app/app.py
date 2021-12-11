from flask import Flask
from flask_cors import CORS
from flask import request, redirect
from flask.templating import render_template
import sqlite3

con = sqlite3.connect('../attendance-system.db',check_same_thread=False)
cursor = con.cursor()

app = Flask('AI-Attendance-System')
CORS(app)
app.run(debug=True)

@app.route('/home')
def home():
    # return 'okay'
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute('SELECT * FROM faculty WHERE name=:username AND password=:password',{"username":username, "password":password})
    account = cursor.fetchone()
    if account:
        query = 'select * from attendance'
        cursor.execute(query)
        response = cursor.fetchall()
        for x in response:
            print(x)
        return render_template('attendance.html',response=response)

    else:
        return redirect('/home')

@app.route('/register')
def register():
    return render_template('index1.html')

@app.route('/photoCapture')
def capture():
    return render_template('photoCapture.html')

@app.route('/upload', methods=['GET', 'POST']) 
def upload():
    return 'Uploaded'


