# from django.test import TestCase
# from master.models.global_models import *
# from master.models.company import *
# import pytest
# import uuid

# from rest_framework.test import APIClient
# from mixer.backend.django import mixer
# from django.urls import reverse

# # for user model

# from user.models import User, UserAccessLogData

# pytestmark = pytest.mark.django_db


# class TestHsnCode(TestCase):
    
#     def setUp(self):
#         self.client = APIClient()
#         print(self.client,"this is self.client")
#         self.hsn_code = mixer.blend(MasterHSNData,name="HSN001")
        
#         self.user = User.objects.create(email="vikash@gmail.com")
        
#         self.token, self.refresh_token = self.user.get_tokens()
        
#         UserAccessLogData.objects.create(user=self.user,login_access_key=self.token,browser_info='abcd')
        
#         print("self.token >>>>",self.token)
        
#         self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.token)
    
#     def test_hsn_code_created(self):
        
#         print("hsn obj >>>>",self.hsn_code)
        
#         # self.assertEqual(self.hsn_code.name,"HSN001")
#         assert str(self.hsn_code.name) == "HSN001"
    
#     def test_hsn_list_api(self):
        
#         response = self.client.get('/api/master/get_hsn_list')
#         print(response.json, "response dir >>>")
        
        
#         assert response.status_code == 200
#         assert response.json != None
#         # assert False
    
#     def test_create_hsn(self):
        
#         input_data = {
#             "name":"HSN004",
#             "hsn_code":"HSN0009"   
#         }
#         url = reverse('hsn_create')
        
#         response = self.client.post(url,data=input_data)
        
#         assert response.json() != None
#         assert response.status_code ==201
    
#     def test_get_hsn_detail(self):
        
#         hsn_1 = mixer.blend(MasterHSNData,id=uuid.uuid4 ,name="HSN002")
#         hsn_2 = mixer.blend(MasterHSNData,id=uuid.uuid4,name="HSN003")
        
#         url1 = reverse('hsn_detail',kwargs={'id':hsn_1.id})
#         url2 = reverse('hsn_detail',kwargs={'id':hsn_1.id})
        
#         response1 = self.client.get(url1)
#         response2 = self.client.get(url2)
        
#         assert response1.json() != None
#         assert response1.status_code == 200
    
#         assert response2.json() != None
#         assert response2.status_code == 200
        
    
    