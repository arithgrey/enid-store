from models_loader import LeadTypeLoader

class LeadType:
        
    def load(self):
            
        data = [
            {'id': 1, 'name': 'Al hacer seguir en contacto'},
            {'id': 2, 'name': 'Al registrar orden'},
            {'id': 3, 'name': 'Al hacer registro'},            
        ]

        LeadTypeLoader(data).load_data()