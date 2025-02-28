from flask import Flask, jsonify

app = Flask("app")

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]


#define students by who is older than 20 
@app.route('/old_students/', methods = ['GET'])
def old_students():
    old_stud_list = []
    for stud in students:
        if stud['age'] > 20:
            old_stud_list.append(stud)
    #return jsonify
    return jsonify(old_stud_list)

#define students by who is younger than 21
@app.route('/young_students/', methods = ['GET'])
def young_students():
    young_stud_list = []
    for stud in students:
        if stud['age'] < 21:
            young_stud_list.append(stud)
    #return jsonify
    return jsonify(young_stud_list)
#define students that have A's and are younger than 21
@app.route('/advanced_students/', methods = ['GET'])
def advanced_students():
    advanced_stud_list = []
    for stud in students:
        if stud['age'] < 21 and stud['grade']  == 'A':
            advanced_stud_list.append(stud)
    #return jsonify
    return jsonify(advanced_stud_list)

#define students first and last names 
@app.route('/student_names/', methods = ['GET'])
def student_names():
    student_name_list = []
    for stud in students:
            student_name_list.append({"First name: ": stud['first_name'], "Last Name: ": stud['last_name']})
    #return jsonify
    return jsonify(student_name_list)

#define studentfirst and last names with ages
@app.route('/student_ages/', methods = ['GET'])
def student_age():
    student_age_list = []
    for stud in students:
        student_name = stud['first_name'] + ' ' + stud['last_name']
        age = stud['age']
        student_age_list.append({student_name: age})
    #return jsonify 
    return jsonify(student_age_list)

#define get all students function
@app.route('/get_students/', methods = ['GET'])
def get_students():
    return jsonify(students)


#execute api in development port 
app.run(debug= True, port = 8000)