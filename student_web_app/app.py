from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

# Make a flask app
app = Flask(__name__)
app.config['DEBUG'] = True

# Set secret key
app.config['SECRET_KEY'] = "your secret key"
"""
Function to request student data from the api
Input: url
Ouput: JSON student data
"""

def get_student_data(url:str):
     # Make a request
     response = requests.get(url)
     
     # Convert response format to JSON
     response_json = response.json()
     return response_json

# Create a route for the website index/root. It will display all student data.
@app.route('/', methods=['GET'])
def index():
     # Make a requst to the student data api
     url = 'http://127.0.0.1:5000/api/students/all'
     student_data = get_student_data(url)
     return render_template('index.html')
# Run the flask application
app.run(port=5001)
