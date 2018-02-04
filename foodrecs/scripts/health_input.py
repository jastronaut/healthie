import health_api as api
import urllib
import recipe

def get_age():
    return int(input("Enter age: "))

def get_height():
    return int(input("Enter height in inches: "))

def get_weight():
    return int(input("Enter weight in lbs: "))

def get_gender():
    gender = input("Enter gender (M/F): ")
    gender = gender.lower()
    if (gender[0] == 'm' ) or (gender[0] == 'f'):
        return gender
    get_gender()

def get_activity():
    print("1 - Light to no exercise \n2 - Light exercise \n3 - Moderate Exercise")
    print("4 - Heavy Exercise \n5 - Very Heavy Exercise")
    act = int(input("Enter activity level (1-5): "))
    if (act > 5 or act < 1):
        get_activity()
    return act
    

def get_calories(gender, age, height, weight, activity):
    '''return revised Harris Benedict equation'''
    if gender[0] == 'm':
        bmr = (10 * lbs_to_kg(weight)) + (6.25 * inch_to_cm(height)) - (5 * age) + 5
    if gender[0] == 'f':
        bmr = (10 * lbs_to_kg(weight)) + (6.25 * inch_to_cm(height)) - (5 * age) - 161
    return round(get_multiplier(activity) * bmr)

def get_multiplier(act):
    if act == 1:
        return 1.2
    if act == 2:
        return 1.375
    if act == 3:
        return 1.55
    if act == 4:
        return 1.725
    if act == 5:
        return 1.9
    
def inch_to_cm(inches):
    return inches * 2.54


def lbs_to_kg(lbs):
    return lbs * 0.453592

def shuffle_meals(saved_json, calorie_goal, meals = ["breakfast", "lunch", "dinner"] ):
    day_list = []
    for meal in meals:
        day_list.append(api.add_recipe(saved_json[meal], calorie_goal))
    return day_list





if __name__ == "__main__":
##    activity = get_activity()
##    print(get_multiplier(activity))
##    gender = get_gender()
##    age = get_age()
##    height = get_height()
##    weight = get_weight()
##    calorie_goal = get_calories(gender, age, height, weight, activity)
##    print("Calorie goal", calorie_goal)
##
    calorie_goal = 2000
    day_list = []
    json_saved = {}

    for meal in ["breakfast", "lunch", "dinner"]:
        url = api.create_url() + "&q=" + meal
        json = api.get_result(url)
        json_saved[meal] = json

    day_list = shuffle_meals(json_saved,calorie_goal)

    total_cals = 0
    for meal in day_list:
        print(meal.name)
        cals = meal['calories']
        print(cals)
        total_cals+=cals
    print("Total Calories:" + str(total_cals))

    for key,value in day_list[0].quants.items():
        print(key, value)


    while input("Shuffle?") == "y":
        day_list = shuffle_meals(json_saved, calorie_goal)
        total_cals = 0
        for meal in day_list:
            print(meal.name)
            cals = meal['calories']
            print(cals)
            total_cals+=cals
        print("Total Calories:" + str(total_cals))
