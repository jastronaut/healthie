from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('foodresults', views.foodresults, name='foodresults'),
	# path('enterinfo', views.enterinfo, name='enterinfo')
]