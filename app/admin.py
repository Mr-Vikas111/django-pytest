from django.contrib import admin
from app.models import *


class SubjectDataAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(SubjectData)


class TeacherDataAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(TeachersData)


class StudentDataAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(StudentData)

class StudentResultDataAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(StudentExamResultData)