from django.db import models

class Cars(models.Model):
    car_types=[
        ('seadan','sedan'),
        ('hatchback','hatchback'),
        ('muv','muv'),
        ('suv','suv'),
        ('electrical','electrical'),
    ]
    fuel_types=[
        ('petrol','petrol'),
        ('diesel','diesel'),
        ('electric','electric'),
        ('hybrid','hybrid'),
    ]
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    year=models.IntegerField()
    car_type=models.CharField(max_length=20,choices=car_types)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    fuel_type=models.CharField(max_length=20,choices=fuel_types)
    mileage=models.DecimalField(max_digits=10,decimal_places=2)
    transmission=models.CharField(max_length=30)
    image=models.ImageField(upload_to='car_images/', blank=True,null=True)
    description=models.TextField(blank=True)
def __str__(self):
    return f"{self.name} - {self.brand}"
