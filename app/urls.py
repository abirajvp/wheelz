from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('home/', views.home,name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('about/', views.about, name="about"),
    path('cars/', views.cars, name="cars"),
    path('car-details/<int:car_id>/', views.car_detail, name="car_detail"),
    path('add-car', views.add_car, name="add-car"),
    path('contact/', views.contact, name="contact"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('team/', views.team, name="team"),
    path('faq/', views.faq, name="faq"),
    path('terms/', views.terms, name="terms"),
    path('add-category', views.add_category, name="add-category"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
]