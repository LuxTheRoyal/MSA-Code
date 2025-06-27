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
     return render_template('index.html', student_data=student_data)

# Create a route for the majors search page
@app.route('/major', methods=['GET'])
def majors_get():
     # Get a list of student data
     url = 'http://127.0.0.1:5000/api/students/all'
     student_data = get_student_data(url)
     # Create a list to store unique majors
     major_list = []
     # Use a for loop to interate through the student list
     for student in student_data:
          # Add major to majors list if major not currently in list
          if student['major'] not in major_list:
               major_list.append(student['major'])
     # Sort the major list
     major_list.sort()
     return render_template('majors.html', major_list=major_list)

# Create a route for the majors search page
@app.route('/major', methods=['POST'])
def majors_post ():
     # Get a list of student data
     url = 'http://127.0.0.1:5000/api/students/all'
     student_data = get_student_data(url)
     # Create a list to store unique majors
     major_list = []
     # Use a for loop to interate through the student list
     for student in student_data:
          # Add major to majors list if major not currently in list
          if student['major'] not in major_list:
               major_list.append(student['major'])

     # Sort the major list
     major_list.sort()
     # Get the form data
     major = request.form.get('major')
     print(f"This is majors{major}")
     # Create the request url to get students with that major
     url = f"http://127.0.0.1:5000/api/major/{major}" 
     # Send the request and get the response 
     result_list = get_student_data(url)
     # Send the results to the majors template
     return render_template('majors.html', major_list=major_list, result_list=result_list)

# Run the flask application
app.run(port=5001)
