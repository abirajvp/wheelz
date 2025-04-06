from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cars(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        search_dict = {}
        cars = Car.objects.filter(**search_dict)
    else:
        cars = Car.objects.all()
        models = Model.objects.all()
        makes = Make.objects.all()
        vehicle_types = VehicleType.objects.all()
        fuels = Fuel.objects.all()
        gearboxes = Gearbox.objects.all()
        context = {
            'cars': cars,
            'models': models,
            'makes': makes,
            'vehicle_types': vehicle_types,
            'fuels': fuels,
            'gearboxes': gearboxes,
            'seat_range': range(1, 10),
            'doors': range(1, 6),
            'engine_range': range(1, 10),
            'power_range': range(1, 500),
        }
    return render(request, 'cars.html', {**context})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car-details.html', {'car': car})

def faq(request):
    return render(request, 'faq.html')

def team(request):
    return render(request, 'team.html')

def teams(request):
    return render(request, 'teams.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def terms(request):
    return render(request, 'terms.html')