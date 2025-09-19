from django.test import TestCase
import pytest
import uuid

# from rest_framework.test import APIClient
from mixer.backend.django import mixer
from django.urls import reverse

from rest_framework.test import APIClient


from app.models import *
import json


pytestmark = pytest.mark.django_db

class StudentModelTestCase(TestCase):
    
    def setUp(self):
        pass
    
    
    def test_subject_create(self):
        subject_1 = mixer.blend(SubjectData,name="Hindi")
        subject_2 = mixer.blend(SubjectData,name="English")
        
        assert subject_1.name == 'Hindi1'
        assert subject_2.name == 'English'
        
        
    def test_student_create(self):
        
        student_obj_1 = mixer.blend(StudentData,name="vikash",subjects=[mixer.blend(SubjectData),mixer.blend(SubjectData)])
        student_obj_2 = mixer.blend(StudentData,name="vishal")
        
        assert student_obj_1.name == "vikash"
        assert student_obj_2.name == "vishal"
        
    def test_teacher_create(self):
        teacher_1 = mixer.blend(TeachersData,name='Rohit',subjects=[mixer.blend(SubjectData,name='Social Science'),mixer.blend(SubjectData,name="Hindi")])
        teacher_2 = mixer.blend(TeachersData,name='Rita',subjects=[mixer.blend(SubjectData,name='Science'),mixer.blend(SubjectData,name="English")])
        
        assert teacher_1.name == "Rohit"
        assert  'Hindi' and 'Social Science' in [subject.name for subject in teacher_1.subjects.all()]
        assert 'English' and 'Science' in [subject.name for subject in teacher_2.subjects.all()]
        assert teacher_2.name == 'Rita'
    
    def test_student_exam_result(self):
        student_exam_result_1 = mixer.blend(StudentExamResultData,student=mixer.blend(StudentData,name="Vicky"),
                                          teacher=mixer.blend(TeachersData,name="Rohan"),
                                          subject=mixer.blend(SubjectData,name="Hindi"),status='Pass')
        
        student_exam_result_2 = mixer.blend(StudentExamResultData,student=mixer.blend(StudentData,name="Vikas"),
                                          teacher=mixer.blend(TeachersData,name="Rohit"),
                                          subject=mixer.blend(SubjectData,name="English"),status='Fail')
        
        assert student_exam_result_1.student.name == "Vicky" 
        assert student_exam_result_1.status == "Pass"
        assert student_exam_result_1.teacher.name == "Rohan"
        assert student_exam_result_1.subject.name == "Hindi"
        
        assert student_exam_result_2.student.name == "Vikas" 
        assert student_exam_result_2.status == "Fail"
        assert student_exam_result_2.teacher.name == "Rohit"
        assert student_exam_result_2.subject.name == "English"
        

class StudentAPITestCases(TestCase):
    
    
    def setUp(self) -> None:
        self.client = APIClient()
    
    
    def test_student_list(self):
        
        mixer.blend(StudentData,name="vikash",subjects=[mixer.blend(SubjectData),mixer.blend(SubjectData)])
        
        response = self.client.get('/student/')
        print("response json",response.json())
        
        assert response.status_code == 200
        assert response.json() != None
    
    def test_student_create(self):
        
        subject_one  = mixer.blend(SubjectData,name="Hindi")
        subject_two = mixer.blend(SubjectData,name="English")

        request_data = {
            'name':'Vijay',
            'subjects':[subject_one.id,subject_two.id],
            'age':25,
            'gender':'Male'
        }
        response = self.client.post('/student/',data=request_data)
        
        print("json_data >>>",response.json())

        assert response.status_code == 201
        assert response.json().get('name') == "Vijay"
        
    
        
        
    