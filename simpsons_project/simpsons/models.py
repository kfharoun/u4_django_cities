from django.db import models

class City(models.Model): 
    name = models.CharField(max_length=100)
    population = models.IntegerField(default=0)
    photo_url = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    photo_url = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Review(models.Model): 
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    photo_url = models.TextField(blank=True)
    description = models.CharField(max_length=200, default='no description')

    def __str__(self):
        return self.name