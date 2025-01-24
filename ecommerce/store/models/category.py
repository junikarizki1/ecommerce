from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='upload/category/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    