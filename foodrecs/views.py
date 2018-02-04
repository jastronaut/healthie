from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CalculateCaloriesForm
from .models import Person

from foodrecs.recipe import *
from foodrecs.health_api import *
from foodrecs.health_input import *

def index(request):
    return render(request, 'foodrecs/index.html')


def enterinfo(request):
    p = Person()
    if request.method == "GET":
        form = CalculateCaloriesForm(request.GET)
        # if form.is_valid():
        p.age = request.GET.get("age")
        print("age is", request.GET.get("age"))
        p.weight = request.GET.get("weight")
        p.height = request.GET.get("height")
        p.activitylevel = request.GET.get("activitylevel")
        p.gender = request.GET.get("gender")
        # p.restrictions = form.cleaned_data["dietRestrictions"]
        p.restrictions = request.GET.get("dietRestrictions")
        p.update_info()
        print("Ok, exiting to next page :) sweety")
        return foodresults(request, p)
            # return HttpResponseRedirect('')
            # return render(request, 'foodrecs/enterinfo.html', {'form': form, 'PageTitle': 'Enter Your Info', 'entered': True})
    # print("Input not valid.")
    # form = CalculateCaloriesForm()
    # return render(request, 'foodrecs/enterinfo.html', {'form': form, 'PageTitle': 'Dang it!'})

def foodresults(request, person):
    calories = get_calories(person.get_info("gender"), person.get_info("age"), person.get_info("height"), person.get_info("weight"), person.get_info("activitylevel"))
    meals = generate_meals(int(calories))

    context = {'totalCalories': calories, 'breakfast': meals[0], 'lunch': meals[1], 'dinner': meals[2], 'person': person}
    context['mealCalories'] = context['breakfast']['calories'] + context['lunch']['calories'] + context['dinner']['calories']

    return render(request, 'foodrecs/foodresults.html', context)