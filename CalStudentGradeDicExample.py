def add_grade(student_grades, student_name, grade):
    """
    Adds a grade for a student to the dictionary.
    
    :param studendt_grades: Dictionary containing student names and their grades
    :param student_name: Name of the student
    :param grade: Grade of the student
    """
    if student_name in student_grades:
        student_grades[student_name].append(grade)
    else:
        student_grades[student_name] = [grade]

def calculate_average(student_grades, student_name):
    """
    Calculates the average grade for a student.
    
    :param student_grades: Dictionary containing student names and their grades
    :param student_name: Name of the student
    :return: Average grade of the student or None if the student is not found
    """
    if student_name in student_grades:
        grades = student_grades[student_name]
        return sum(grades) / len(grades)
    else:
        return None
    
def main():
    student_grades = {}
    
    # Adding grades for students
    add_grade(student_grades, 'Alice', 85)
    add_grade(student_grades, 'Bob', 90)
    add_grade(student_grades, 'Alice', 95)
    
    # Calculating average grades
    alice_avg = calculate_average(student_grades, 'Alice')
    bob_avg = calculate_average(student_grades, 'Bob')
    
    print(f"Alice's average grade: {alice_avg}")
    print(f"Bob's average grade: {bob_avg}")

main()