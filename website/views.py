from django.shortcuts import render
from .models import Person

# Create your views here.
def home(request):
    trainers = Person.objects.filter(category='Trainer')
    trainees = Person.objects.filter(category='Trainee')
    return render(request, 'home.html', {
        'trainers': trainers,
        'trainees': trainees
    })