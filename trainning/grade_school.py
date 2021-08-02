#Given students' names along with the grade that they are in, create a roster for the school.

#In the end, you should be able to:

#Add a student's name to the roster for a grade
#"Add Jim to grade 2."
#"OK."
#Get a list of all students enrolled in a grade
#"Which students are in grade 2?"
#"We've only got Jim just now."
#Get a sorted list of all students in all grades. Grades should sort as 1, 2, 3, etc., and students within a grade should be sorted alphabetically by name.
#"Who all is enrolled in school right now?"
#"Grade 1: Anna, Barb, and Charlie. Grade 2: Alex, Peter, and Zoe. Grade 3…"
#Note that all our students only have one name. (It's a small town, what do you want?)

class School:
    def __init__(self):
        self.students = {}


    def add_student(self, name, grade):
        self.students[name] = grade


    def roster(self):
        # self.roster = dict(sorted(self.students.items(), key=lambda item: item[1]))
        roster_list = []
        for grade in range(0,8):
            roster_list +=self.grade(grade)

        return roster_list

    def grade(self, grade_number):
        grade_list = []
        for key, value in self.students.items():
            if value == grade_number:
                grade_list.append(key)
        grade_list.sort()
        if grade_list:
            return grade_list
        else:
            return []

school()