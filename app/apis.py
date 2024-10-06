from django.shortcuts import render 
from django.http import Http404 

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from app.serializers import *
from app.models import *




""" #### ->>>>>>>>>>>. Subject All APIs ->>>>>>>>>>>>>>>>####"""
class SubjectListAPIView(APIView):
	
    def get(self, request, format=None):
        queryset = SubjectData.objects.all()
        serializer = SubjectSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            
		
class SubjectDetailAPIView(APIView): 
	""" 
	Retrieve, update or delete a transformer instance 
	"""
	def get_object(self, id): 
		# Returns an object instance that should 
		# be used for detail views. 
		try: 
			return SubjectData.objects.get(id=id) 
		except SubjectData.DoesNotExist: 
			raise Http404 

	def get(self, request, id, format=None): 
		transformer = self.get_object(id) 
		serializer = SubjectSerializer(transformer) 
		return Response(serializer.data) 

	def patch(self, request, id, format=None): 
		transformer = self.get_object(id) 
		serializer = SubjectSerializer(transformer, 
										data=request.data, 
										partial=True) 
		if serializer.is_valid(): 
			serializer.save() 
			return Response(serializer.data) 
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
		

	def delete(self, request, id, format=None): 
		transformer = self.get_object(id) 
		transformer.delete() 
		return Response(status=status.HTTP_200_OK)

""" #### ->>>>>>>>>>>. Student All APIs ->>>>>>>>>>>>>>>>####"""
class StudentListAPIView(APIView):
	
    def get(self, request, format=None):
        queryset = StudentData.objects.all()
        serializer = StudentSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
		
class StudentDetailAPIView(APIView): 
	""" 
	Retrieve, update or delete a transformer instance 
	"""
	def get_object(self, id): 
		# Returns an object instance that should 
		# be used for detail views. 
		try: 
			return StudentData.objects.get(id=id) 
		except StudentData.DoesNotExist: 
			raise Http404 

	def get(self, request, id, format=None): 
		transformer = self.get_object(id) 
		serializer = StudentSerializer(transformer) 
		return Response(serializer.data) 

	def patch(self, request, id, format=None): 
		transformer = self.get_object(id) 
		serializer = StudentSerializer(transformer, 
										data=request.data, 
										partial=True) 
		if serializer.is_valid(): 
			serializer.save() 
			return Response(serializer.data) 
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
		

	def delete(self, request, id, format=None): 
		transformer = self.get_object(id) 
		transformer.delete() 
		return Response(status=status.HTTP_200_OK)


""" ### ->  Teacher APIs ########"""
class TeacherListAPIView(APIView):
	
    def get(self, request, format=None):
        queryset = TeachersData.objects.all()
        serializer = TeacherSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
		
class TeacherDetailAPIView(APIView): 
	""" 
	Retrieve, update or delete a transformer instance 
	"""
	def get_object(self, id): 
		# Returns an object instance that should 
		# be used for detail views. 
		try: 
			return TeachersData.objects.get(id=id) 
		except TeachersData.DoesNotExist: 
			raise Http404 

	def get(self, request, id, format=None): 
		transformer = self.get_object(id) 
		serializer = TeacherSerializer(transformer) 
		return Response(serializer.data) 

	def patch(self, request, id, format=None): 
		transformer = self.get_object(id) 
		serializer = TeacherSerializer(transformer, 
										data=request.data, 
										partial=True) 
		if serializer.is_valid(): 
			serializer.save() 
			return Response(serializer.data) 
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
		

	def delete(self, request, id, format=None): 
		transformer = self.get_object(id) 
		transformer.delete() 
		return Response(status=status.HTTP_200_OK)
