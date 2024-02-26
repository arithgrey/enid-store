from django.test import TestCase

class ValidatorTest(TestCase):

    def setUp(self):
        self.serializer_class = None
        self.required_fields = [] 
        self.not_allow_blank = [] 
        self.max_lengths = {}
        self.min_lengths = {}
        self.min_values = {}
        self.max_values = {}

    def test_required_fields(self):    
        
        for field in self.required_fields:
            data = {}                            
            serializer = self.serializer_class(data=data)      
            self.assertFalse(serializer.is_valid())
            self.assertIn(field, serializer.errors)
    
    
    def test_not_allow_blank(self):        

        for field in self.not_allow_blank:
            data = {field: ''}
            serializer = self.serializer_class(data=data)                                        
            self.assertFalse(serializer.is_valid())            
            self.assertIn(field, serializer.errors)
            self.assertEqual(serializer.errors[field][0].code, 'blank')

    def test_error_over_max_length(self):
        for field, value in self.max_lengths.items():
            max_length = value + 1                      
            data = {field: 'a' * max_length}
            serializer = self.serializer_class(data=data)
            self.assertFalse(serializer.is_valid())        
            self.assertIn(field, serializer.errors)
    
    def test_error_on_min_length(self):
        for field, value in self.min_lengths.items():
            min_length = value - 1                      
            data = {field: 'a' * min_length}
            serializer = self.serializer_class(data=data)
            self.assertFalse(serializer.is_valid())        
            self.assertIn(field, serializer.errors)
    
    def test_error_on_min_value(self):        
        #Debe marcar error siempre que el numero sea menor a 
        for field, value in self.min_values.items():            
            min_value = value - 1
            data = {field: min_value}
            serializer = self.serializer_class(data=data)                            
            self.assertFalse(serializer.is_valid())
            self.assertIn(field, serializer.errors)            
            self.assertEqual(serializer.errors[field][0].code, 'min_value')
    
    def test_error_over_max_value(self):
        #Debe marcar error siempre que el numero sea menor a 
        for field, value in self.max_values.items():            
            min_value = value + 1
            data = {field: min_value}
            serializer = self.serializer_class(data=data)                            
            self.assertFalse(serializer.is_valid())
            self.assertIn(field, serializer.errors)            
            self.assertEqual(serializer.errors[field][0].code, 'max_value')


