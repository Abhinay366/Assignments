#Student data using pickling and unpickling.
import pickle
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def save_student_data(studata, student):
    with open(studata, 'wb') as file:#Function to pickle student data to a file.
        pickle.dump(student, file)
    print(f"Student data saved to {studata}")

def load_student_data(studata):
    with open(studata, 'rb') as file:#Function to unpickle student data from a file.
        student = pickle.load(file)
    return student

student1 = Student("Abhi", 23, "A")#Creating an instance of the Student data.

save_student_data("student_data.pickle", student1)#Saving student data to a file using pickling.

loaded_student = load_student_data("student_data.pickle")#loading student data to file using unpickling.

print("Loaded student data:")#Displaying loaded student data.
print(f"Name: {loaded_student.name}, Age: {loaded_student.age}, Grade: {loaded_student.grade}")

 