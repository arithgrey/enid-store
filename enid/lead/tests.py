from django.test import TestCase
from rest_framework.test import APIClient
from lead.models import Lead
from lead_type.models import LeadType
from faker import Faker
from share_test.commons import CommonsTest

class TestsLeadViewSet(TestCase):
    def setUp(self):
        self.fake = Faker('es_MX')
        self.client = APIClient()
        self.lead_type = LeadType.objects.create(name="En intento de compra")
        self.commons = CommonsTest()

    
    def fake_user(self, create_object=False):
        lead_type_id = self.lead_type.id
        
        user = {
            "email": self.fake.email(), 
            "name": self.fake.name(),
            "phone_number": self.fake.phone_number().split('x')[0].strip(),
            "lead_type": lead_type_id,            
        }
        
        if not create_object:
            return user
        
        lead_type = LeadType.objects.get(id=lead_type_id)
        user["lead_type"] = lead_type
        
        
        obj = Lead.objects.create(**user)

        return obj

    def test_success_create_lead_with_interest_products(self):
        
        first_product = self.commons.create_fake_product()
        second_product = self.commons.create_fake_product()
                
        fake_lead = self.fake_user()
        fake_lead['products_interest'] = [first_product.id, second_product.id]
               
        response = self.client.post('/api/lead/existence/', fake_lead, format='json')        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Lead.objects.count(), 1)
        self.assertEqual(response.data["products_interest"], [first_product.id, second_product.id])

    
    def test_success_create_lead(self):
                        
        response = self.client.post(
            '/api/lead/existence/', self.fake_user(), format='json')          
        
        self.assertEqual(response.status_code, 201)        
        self.assertEqual(Lead.objects.count(),1)


    def test_success_handler_response_400s(self):
                        
        response = self.client.post(
            '/api/lead/existence/', {}, format='json')                                            
        self.assertEqual(response.status_code, 400)        
        

    def test_success_add_triet_lead(self):
                        
        fake_lead  = self.fake_user(create_object=True)
        self.assertEqual(fake_lead.tryet, 1)
        
        lead_type = fake_lead.lead_type.id
        data = {
            'email': fake_lead.email,
            'lead_type':lead_type,
            'name':fake_lead.name ,
            'phone_number':'5552967027',
            }
                
        response = self.client.post(
            '/api/lead/existence/', data, format='json')          
        
        self.assertEqual(response.data["tryet"], 2)
        self.assertEqual(response.status_code, 200)        
        self.assertEqual(response.data["phone_number"], "5552967027")
        self.assertEqual(Lead.objects.count(),1)
        

    def test_success_create_lead_when_diferent_type(self):

        fake_lead  = self.fake_user(create_object=True)                        
        other_type = LeadType.objects.create(name="other type")
        email = fake_lead.email
        
        self.assertEqual(Lead.objects.filter(email=email).count(),1)

        data = {
            'email': email,
            'lead_type':other_type.id,
            'name':fake_lead.name ,
            'phone_number':'5552967027',
            }
                
        response = self.client.post(
            '/api/lead/existence/', data, format='json')          
        
        
        self.assertEqual(response.data["tryet"], 1)
        self.assertEqual(response.status_code, 201)        
        self.assertEqual(email, response.data["email"])
        self.assertEqual(Lead.objects.filter(email=email).count(),2)