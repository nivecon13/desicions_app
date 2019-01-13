from django.urls import path

from . import views

#this tells django templates what url to use if other apps have same url names
#app_name = 'weate'

app_name = 'food'
urlpatterns = [
    path('restaurant', views.NewRestaurantView, name='NewRestaurant')]