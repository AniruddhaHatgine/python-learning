class users:
    Email="a@b.com"
    phone=7058054406
    education="BCA"
    role="Student"

class enroll:
    userNO :1
    courseNo :1
    
class Course:
    CourseName="Python"
    CourseDuration="3 month"
    CourseFee=5000
    courseNO=1

class Modules(Course):
    ModuleNo=1
    ModuleTitle="Basic pyhton" 
    ModuleDescr="Desc"
    courseNO=1

class assignement(Modules):
    AssignmentNO=1
    AssignmentTitle="Assign 1"
    Modules.Module=1


guru = users() #2
aniruddha = users() #1

Course1=Course()
assignement=assignement()






