from django import forms
from django.db import models

class CalculateCaloriesForm(forms.Form):
	GENDERS = (
		("m", "Male"),
		("f", "Female")
	)
	ACTIVITY_LEVEL = (
		(1, "Sedentary"),
		(2, "Light Exercise, 1-2 days/week"),
		(3, "Moderate Exercise, 3-5 days/week"),
		(4, "Heavy Exercise, 6-7 days/week"),
		(5, "Athlete, 2 times/day")
	)

	RESTRICTIONS = (
		("d_balanced", "Balanced"),
		("d_low-carb", "Low-Carb"),
		("d_low-fat", "Low-Fat"),
		("d_high-protein", "High-Protein"),
		("h_peanut-free", "Peanut-Free"),
		("h_alcohol-free", "Alcohol-Free"),
		("h_tree-nut-free", "Tree-Nut-Free"),
		("h_sugar-conscious", "Sugar Conscious")
	)

	# gender = forms.ChoiceField(label="Gender (M/F)", required=True, choices=THE_ONLY_GENDERS)
	# weight = forms.FloatField(label="Weight (lbs)", required=True, min_value=1)
	# height = forms.IntegerField(label="Height (in)", required=True, min_value=12)
	# age = forms.IntegerField(label="Age (yrs)", required=True, min_value=12)
	# activitylevel = forms.ChoiceField(label="Activity Level", required=True, choices=ACTIVITY_LEVEL)

	gender = forms.ChoiceField(label="Gender (M/F)", choices=GENDERS, initial="M")
	weight = forms.FloatField(label="Weight (lbs)", min_value=1, initial=140)
	height = forms.IntegerField(label="Height (in)", min_value=12, initial=68)
	age = forms.IntegerField(label="Age (yrs)", min_value=12, initial=19)
	activitylevel = forms.ChoiceField(label="Activity Level", choices=ACTIVITY_LEVEL, initial=1)
	dietRestrictions = forms.MultipleChoiceField(label="Dietary Restrictions", choices=RESTRICTIONS, widget=forms.CheckboxSelectMultiple(), required=False)
