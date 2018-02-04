import json
import urllib.parse
import urllib.request
import recipe
import random

APP_ID = "d9879cd6"
API_KEY = "b2611f54e41c478b690f2182fa36db22"
URL_BASE = "https://api.edamam.com/search?"


def create_url():
    return URL_BASE + "&app_id=" + APP_ID + "&app_key=" + API_KEY + "&to=150"

def add_health_restrictions(url:str, flags:list):
    ''' rest [dairy-free, kosher, kidney-friendly, etc] ''' 
    for rest in flags:
        url+="&Health=" + rest
    return url

def add_diet_restrictions(url:str, flags:list):
    ''' rest [ balanced, high-fiber, low-carb, etc'''
    for rest in flags:
        url+="&Diet=" + rest
    return url
        


def get_result(url: str)->dict:
    '''this will recieve the json text'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()



def add_recipe(json:dict, cal_goal:int):
    choice = random.randrange(0, len(json['hits']))
    r = recipe.Recipe(json['hits'][choice])
    while (r['calories'] > cal_goal/3) or (r['calories'] < 300):
        choice = random.randrange(0, len(json['hits']))
        r = recipe.Recipe(json['hits'][choice])    
    return r





