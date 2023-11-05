student = {'Name': 'Dipan', 'Age': 19, 'Level': "Bachelor's"}
student['Courses'] = ["Physics", "Math", "Chemistry"]
student.update({'Name': 'Gribani', "Courses": ["Bruh"]})
x =  student.pop('Name')
for key, value in student.items():
    print(key, value)