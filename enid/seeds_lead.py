from models_loader import LeadTypeLoader

class LeadType:
        
    def load(self):
            
        data = [
            {
                "id":1,
                "name": '''Kit de pesas con barra z, recta y mancuernas''',                    
            },                                   
            {
                "id":2,
                "name": '''Kit de pesas con barra z, Romana, recta y mancuernas''',                    
            },  
            {
                "id":3,
                "name": '''Solo mancuernas''',                    
            },                                   
        ]

        LeadTypeLoader(data).load_data()