from flask import Flask
from flask_cors import CORS
from flask import request, redirect
from flask.templating import render_template
import mysql.connector

mydb = mysql.connector.connect(
  host="ai-attendance-devjam.c92vkw0v7cnn.ap-south-1.rds.amazonaws.com",
  user="admin",
  passwd="admin123",
  database="test1"
)
cursor = mydb.cursor()

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
    # print(username,password)
    cursor.execute('SELECT * FROM faculty WHERE name = (%s) AND password = (%s)',(username,password,))
    account = cursor.fetchone()
    print(account)
    for x in cursor:
        print(x)
    if account:
        return "Logged in"
    else:
        return "Nikal"

@app.route('/register')
def register():
    return render_template('index1.html')

@app.route('/photoCapture')
def capture():
    return render_template('photoCapture.html')

@app.route('/upload', methods=['GET', 'POST']) 
def upload():
    return 'Uploaded'

# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response

