from rest_framework import serializers
from app.models import *
from app.helpers import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= SubjectData
        exclude=['created','modified']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        exclude = ['created','modified']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersData
        exclude = ['created','modified']