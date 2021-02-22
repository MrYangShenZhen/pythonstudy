import pickle,hashlib
class Base:
    def save(self):
        with open('school.db','wb') as f:
            pickle.dump(self,f)
class School(Base):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
class Course(Base):
    def __init__(self,name,date,price,school):
        self.name=name
        self.date=date
        self.price=price
        self.price=price
class Classroom(Base):
    def __init__(self,course,teacher):
        self.course=course
        self.teacher=teacher
class Student(Base):
    def __init__(self,classroom):#选择学校
        self.classroom=classroom
class Teacher(Base):
    def __init__(self,school):
        self.school=school
f=School('东莞理工','松山湖')
f.save()
s=pickle.load(open('school.db','rb'))
print(s.name)

