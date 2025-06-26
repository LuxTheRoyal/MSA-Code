import flask
from flask import request, jsonify
import student_generator_v2 as sg

# Create a flask app object
app = flask.Flask(__name__)

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True

"""
Function to query the student dictionaries based on a search key.
Input: Search Key
Output: List of results
"""
def search_student_data(search_value, search_key):
     student_dictionaries = sg.get_student_dictionaries()
     print(student_dictionaries)
     list_of_results = []
     for student in student_dictionaries:
          if search_value.lower() == student[search_key].lower(): 
               list_of_results.append(student)
     return list_of_results          
          
# Load student dictionaries

# Create a route 
@app.route("/", methods = ["GET"])
def index():
     return "<h1> Hi my name is Alexander Bates! <h1>"

# Create a route to return all student data
     # Load student dictionaries
# Create 2 routes
# 1 - Return all student data
@app.route("/api/students/all", methods = ["GET"])
def api_all():
     student_dictionaries = sg.get_student_dictionaries()
     return jsonify(student_dictionaries)
# 2 - Return students by major
@app.route("/api/major/<string:major>", methods = ["GET"])
def api_students_by_major(major:str):
     major_students = search_student_data(major, "major")
     return jsonify (major_students)
          # Probably going to start using single quotes rather than double for speed purposes
     # Create a route that returns a student based on an id url number
@app.route('/api/students/<string:id>', methods = ['GET'])
def api_student_by_id(id:str):
     student_dictionaries = sg.get_student_dictionaries()
     target_student = None
     # Search student dictionries 
     for student in student_dictionaries:
          if student['id'] == id:
               target_student = student
               break
     return jsonify (target_student)

@app.route('/api/students/class/<string:class_rank>', methods = ['get'])
def api_students_by_class_rank(class_rank:str):
     students_by_class_rank = search_student_data(class_rank, "class")
     return jsonify(students_by_class_rank)
app.run()