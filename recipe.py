class Recipe:
	def __init__(self, info):
		self.info = info
		self.name = self.get_name()
		self.servings = self.get_servings()
		self.quants = self.create_quant_dict()
		self.image = self.get_image_url()
		self.recipe_url = self.get_recipe()

	def get_servings(self):
		return int(self.info['recipe']['yield'])

	def get_image_url(self):
		return self.info['recipe']['image']

	def get_recipe(self):
		return self.info['recipe']['url']





	def get_name(self):
		return self.info['recipe']['label']

	def create_quant_dict(self):
		q = {}
		q['calories'] = round(int(self.info['recipe']['calories']/self.servings))
		for nutrient in self.info['recipe']['totalNutrients']:
			#print(self.info['recipe']['totalNutrients'][nutrient]['label'])
			q[self.info['recipe']['totalNutrients'][nutrient]['label'].lower()] = \
			round(int(self.info['recipe']['totalNutrients'][nutrient]['quantity']/self.servings))
		return q

	def __getitem__(self,key):
		#print(self.quants)
		return self.quants[key.lower()]

	#recipe.get_quantity(calories)



