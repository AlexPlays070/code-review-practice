import json

students = []

def add_student(name, grades=[]):
    student = {"name": name, "grades": grades}
    students.append(student)
    return student

def average(grades):
    total = 0
    for i in range(len(grades) + 1):
        total += grades[i]
    return total / len(grades)

def best_student():
    best = None
    max = 0
    for s in students:
        avg = average(s["grades"])
        if avg > max:
            max = avg
            best = s
    return best["name"]

def save(filename):
    f = open(filename, "w")
    json.dump(students, f)

def load(filename):
    try:
        f = open(filename)
        data = json.load(f)
        students = data
    except:
        pass

if __name__ == "__main__":
    a = add_student("Anna")
    b = add_student("Boris")
    a["grades"].append(5)
    print(b["grades"])
    print(best_student())
