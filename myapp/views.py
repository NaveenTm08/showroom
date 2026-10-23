from django.shortcuts import render
from .models import Cars

# Create your views here.
def home(request):
    cars = Cars.objects.all()
    car_types = request.GET.get('car_type')
    max_price = request.GET.get('max_price')
    if car_types:
        cars = cars.filter(car_type=car_types)
    if max_price:
        try:
            max_price = float(max_price)
            cars = cars.filter(price__lte=max_price)
        except (ValueError, TypeError):
            pass
    return render(request, 'home.html', {'cars': cars, 'car_types': car_types})
def car_detail(request, car_id):
    car = Cars.objects.get(id=car_id)
    return render(request, 'cars_details.html', {'car': car})