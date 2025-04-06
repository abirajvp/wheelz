from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    cars = Car.objects.filter(display_home=True).order_by('-id')[:3]
    return render(request, 'home.html', {'cars': cars})

def dashboard(request):
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_superuser:
        import base64
        name = request.POST.get('name')
        vehicle_id = request.POST.get('vehicle_id')
        price_amount = request.POST.get('price_amount')
        price_display = request.POST.get('price_display')
        price_description = request.POST.get('price_description')
        new_used = request.POST.get('new_used')
        new_car = used_car = False
        if new_used == 'new_car': new_car = True
        elif new_used == 'used_car': used_car = True
        make = request.POST.get('make')
        vechicle_type = request.POST.get('vechicle_type')
        gear = request.POST.get('gear')
        fuel = request.POST.get('fuel')
        vehicle_mode = request.POST.get('vehicle_mode')
        automatic = manual = False
        if vehicle_mode == 'automatic': automatic = True
        if vehicle_mode == 'manual': manual = True
        model = request.POST.get('model')
        doors = request.POST.get('doors')
        seats = request.POST.get('seats')
        mileage = request.POST.get('mileage')
        mileage_display = request.POST.get('mileage_display')
        engine = request.POST.get('engine')
        power = request.POST.get('power')
        color = request.POST.get('color')
        registration_date = request.POST.get('registration_date')
        year = request.POST.get('year')
        owner_name = request.POST.get('owner_name')
        owner_phone = request.POST.get('owner_phone')
        owner_address = request.POST.get('owner_address')
        display_home = request.POST.get('display_home')
        display_home = True if display_home == 'yes' else False
        image = base64.b64encode(request.FILES['image'].read()).decode('utf-8')
        make = Make.objects.filter(id=make).first()
        vechicle_type = VehicleType.objects.filter(id=vechicle_type).first()
        model = Model.objects.filter(id=model).first()
        fuel = Fuel.objects.filter(id=fuel).first()
        gear = Gearbox.objects.filter(id=gear).first()
        car = Car(
            name=name,
            vehicle_id=vehicle_id,
            price_amount=price_amount,
            price_display=price_display,
            price_description=price_description,
            new_car=new_car,
            used_car=used_car,
            automatic=automatic,
            manual=manual,
            make=make,
            vehicle_type=vechicle_type,
            model=model,
            fuel=fuel,
            gearbox=gear,
            doors=doors,
            seats=seats,
            mileage=mileage,
            mileage_display=mileage_display,
            engine=engine,
            power=power,
            color=color,
            registration_date=registration_date,
            year=year,
            owner_name=owner_name,
            owner_phone=owner_phone,
            owner_address=owner_address,
            display_home=display_home,
            image_src=image,
        )
        car.save()
        return redirect('dashboard')
    if request.user.is_authenticated and request.user.is_superuser:
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
            'categories': ['Vehicle Type', 'Make', 'Model', 'Fuel', 'Gear'],
        }
        return render(request, 'dashboard.html', {**context})
    else:
        return redirect('signout')

def add_category(request):
    if request.method == 'POST':
        category = request.POST.get('category_type')
        category_value = request.POST.get('category_value')
        print(category, category_value)
        if category == 'Vehicle Type':
            VehicleType.objects.create(name=category_value)
        elif category == 'Make':
            Make.objects.create(name=category_value)
        elif category == 'Model':
            Model.objects.create(name=category_value)
        elif category == 'Fuel':
            Fuel.objects.create(name=category_value)
        elif category == 'Gear':
            Gearbox.objects.create(name=category_value)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def add_car(request):
    if request.method == 'POST':
        import base64
        name = request.POST.get('name')
        name = request.POST['name']
        vehicle_id = request.POST.get('vehicle_id')
        price_amount = request.POST.get('price_amount')
        price_display = request.POST.get('price_display')
        price_description = request.POST.get('price_description')
        new_used = request.POST.get('new_used')
        make = request.POST.get('make')
        vehicle_mode = request.POST.get('vehicle_mode')
        gear = request.POST.get('gear')
        fuel = request.POST.get('fuel')
        vehicle_mode = request.POST.get('vehicle_mode')
        model = request.POST.get('model')
        doors = request.POST.get('doors')
        seats = request.POST.get('seats')
        mileage = request.POST.get('mileage')
        mileage_display = request.POST.get('mileage_display')
        engine = request.POST.get('engine')
        power = request.POST.get('power')
        color = request.POST.get('color')
        registration_date = request.POST.get('registration_date')
        year = request.POST.get('year')
        owner_name = request.POST.get('owner_name')
        owner_phone = request.POST.get('owner_phone')
        owner_address = request.POST.get('owner_address')
        display_home = request.POST.get('display_home')
        image = base64.b64encode(request.FILES.get('image').read()).decode('utf-8')
        car = Car(
            name=name,
            vehicle_id=vehicle_id,
            price_amount=price_amount,
            price_display=price_display,
            price_description=price_description,
            new_car=new_used,
            used_car=new_used,
            make=Make.objects.get(id=make),
            vehicle_type=VehicleType.objects.get(id=vehicle_mode),
            model=Model.objects.get(id=model),
            fuel=Fuel.objects.get(id=fuel),
            gearbox=Gearbox.objects.get(id=gear),
            doors=doors,
            seats=seats,
            mileage=mileage,
            mileage_display=mileage_display,
            engine=engine,
            power=power,
            color=color,
            registration_date=registration_date,
            year=year,
            owner_name=owner_name,
            owner_phone=owner_phone,
            owner_address=owner_address,
            display_home=display_home,
            image_src=image,
        )
        print(car)
        car.save()
        return JsonResponse({'status': 'success'})


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

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials'})
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect('home')    

