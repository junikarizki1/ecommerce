from django.db import models
class Costumer(models.Model):
    name= models.CharField(max_length=50)
    phone= models.CharField(max_length=15)
    
    def register(self):
        self.save()
        
# biar nomor telepon tidak boleh sama
    def isExists(self):
        if Costumer.objects.filter(phone=self.phone):
            return True
        else:
            return False
