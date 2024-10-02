from django.db import models
import uuid
from decimal import Decimal

"""##### BASE MODEL #########"""
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False,unique=True)
    created = models.DateTimeField(auto_now_add=True, help_text="When this instance was created.")
    modified = models.DateTimeField(auto_now=True, help_text="When this instance was modified.")
    
    class Meta:
        abstract = True
"""######## CHOICES ###########"""

class GenderTypeChoices(models.Choices):
        MALE = 'Male' 
        FEMALE ='Female'


"""######## MAIN MODEL ##########"""

class SubjectData(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.name)
    
class TeachersData(BaseModel):
    name = models.CharField(max_length=120)
    subjects = models.ManyToManyField(to = SubjectData,related_name='_teacher_subjects')
    age = models.FloatField()
    gender = models.CharField(max_length=120,choices=GenderTypeChoices.choices)
    
    def __str__(self) -> str:
        return str(self.name)

class StudentData(BaseModel):
    name = models.CharField(max_length=120)
    subjects = models.ManyToManyField(to = SubjectData,related_name='_student_subjects')
    age = models.FloatField()
    gender = models.CharField(max_length=120,choices=GenderTypeChoices.choices)
    
    def __str__(self) -> str:
        return str(self.name)
    
class StudentExamResultData(BaseModel):
    student = models.ForeignKey(StudentData,on_delete=models.CASCADE,related_name="_student_result")
    teacher = models.ForeignKey(TeachersData,on_delete=models.CASCADE,related_name="_student_result")
    subject = models.ForeignKey(SubjectData,on_delete=models.CASCADE,related_name="_student_result")
    marks = models.FloatField(default=0.0)    
    def set_marks(self, value):
        # Convert to Decimal if it’s a float
        self.marks = Decimal(str(value))
    
    def __str__(self) -> str:
        return f"Student Name : {self.student.name}, Teacher Name: {self.teacher.name}, Subject Name: {self.subject.name},Total Marks: 100, Obtained marks : {self.marks}"

    