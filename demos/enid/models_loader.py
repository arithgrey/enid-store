import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enid.settings")
django.setup()

from faqs.models import Faq
from returns.models import Returns

class DataLoader:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def load_data(self):
        for item in self.data:
            if not self.model.objects.filter(**item).exists():
                self.model.objects.create(**item)

class FaqsLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Faq, data)

class ReturnsLoader(DataLoader):
    def __init__(self, data):
        super().__init__(Returns, data)