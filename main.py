import json

students = []

def add_student(name, grades=None):
    if grades is None:
        grades = []
    student = {"name": name, "grades": list(grades)}
    students.append(student)
    return student

def average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def best_student():
    if not students:
        return None
    best = max(students, key=lambda s: average(s["grades"]))
    return best["name"]

def save(filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False)

def load(filename):
    global students
    try:
        with open(filename, encoding="utf-8") as f:
            students = json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except json.JSONDecodeError:
        print(f"Файл {filename} повреждён")

if __name__ == "__main__":
    a = add_student("Anna")
    b = add_student("Boris")
    a["grades"].append(5)
    print(b["grades"])      # []
    print(best_student())   # Anna
