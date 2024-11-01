from app.models import *
from django.db.models import OuterRef, Subquery

def run():
    
    # check teacher wise pass student 
    
    # teacher = TeachersData.objects.all()
    
    # pass_student = StudentExamResultData.objects.filter(teacher=OuterRef('pk'),marks__gt=50)
    
    # result = teacher.annotate(
    #     pass_student = Subquery(pass_student.values('marks')),
    #     student = Subquery(pass_student.values('student')),
        
    # )
    # print("result >>>",result)
    
    # for re in result:
    #     print("re >>>", re.pass_student,"id >>>>",re.id )
    #     print("re student >>>", re.student)
    
    # subject wise pass student 
    
    student_data = StudentData.objects.all()
    
    pass_student = StudentExamResultData.objects.filter(student=OuterRef('pk'),marks__gt=50)
    
    res_data = student_data.annotate(
        marks_gt = Subquery(pass_student.values(''))
    )
    
    for res in res_data:
        print("res >>>>", res.name)
    
    
    # check subject wise highest score
    
    print("hello world")