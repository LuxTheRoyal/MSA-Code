import flask
from flask import request, jsonify
import student_generator_v2 as sg

# Create a flask app object
app = flask.Flask(__name__)

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True

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
@app.route("/api/majors/<string:major>", methods = ["GET"])
def api_students_by_major(major:str):
     student_dictionaries = sg.get_student_dictionaries()
     print(student_dictionaries)
     major_students = []
     for student in student_dictionaries:
          if major.lower() == student['major'].lower(): 
               major_students.append(student)
          # Probably going to start using single quotes rather than double for speed purposes
     print(major_students)
     return jsonify(major_students)
app.run()