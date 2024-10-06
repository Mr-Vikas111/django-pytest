from django.urls import path
from app.apis import *

urlpatterns = [
    # -> api for student cred  
    path('student/', StudentListAPIView.as_view()), 
    path('student/<str:id>/', StudentDetailAPIView.as_view()), 
    
    # -> api for subject cred  
    path('subject/', SubjectListAPIView.as_view()), 
    path('subject/<str:id>/', SubjectDetailAPIView.as_view()), 
    
    # -> api for teacher cred
    path('teacher/', TeacherListAPIView.as_view()), 
    path('teacher/<str:id>/', TeacherDetailAPIView.as_view()), 
]
