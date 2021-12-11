from flask import Flask
from flask_cors import CORS
from flask.templating import render_template
from flask_cors.decorator import cross_origin

app = Flask('AI-Attendance-System')
CORS(app)
app.run(debug=True)

@app.route('/home')
def home():
    # return 'okay'
    return render_template('index.html')

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

