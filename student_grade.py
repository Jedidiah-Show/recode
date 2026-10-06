Grade={
     70: "A",
     60: "B",
     50: "C",
     45: "D",
     40: "E",
     0: "F"
}

def get_grade(score):
    for key, grade in Grade.items():
        if score >= key:
            return grade
    
def grade_for(students):
    names, averages, grades = [], [], []
    for student in students:
        names += student.get("name", "")
        scores += student.get("scores", [])
        average += [avg for score in scores avg:+=score] 
        grades += get_grade(average)

    student_grades = list(map(lambda x,y,z: (x,y,z), names, averages, grades))
    student_grades_text= list(map(lambda x: f"{x[0]} → Average: {x[1]} → Grade: {x[2]}", student_grades)))
    top_performers= list(map(lambda x: x[0]: x[1], filter(lambda x: x[2] in "ABC", student_grades)))
    
