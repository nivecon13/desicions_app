from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import forms, models
# Create your views here.
def NewRestaurantView(request):
    if request.method == 'POST':
        form = forms.RestaurantForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            r = models.Restaurants(
                restaurant_name=form.cleaned_data['restaurant_name_text'],
                restaurant_city=form.cleaned_data['restaurant_city_text'],
                restaurant_type=form.cleaned_data['restaurant_type_text'],
                what_we_ate=form.cleaned_data['what_we_ate_text'],
                when_we_ate=form.cleaned_data['when_we_ate_text'],
                meal_cost=form.cleaned_data['meal_cost_text'],
                rating_michael=form.cleaned_data['rating_michael_text'],
                rating_coly=form.cleaned_data['rating_coly_text'],
                would_come_again=form.cleaned_data['would_come_again_text'],
                )
            r.save()
            return HttpResponseRedirect(reverse('NewRestaurant'))
    else:
        form = forms.RestaurantForm()
        latest_restaurants = models.Restaurants.objects.order_by('-when_we_ate')
        total_resstaurants = models.Restaurants.objects.count()
        context = {'form': form,
                   'latest_restaurants': latest_restaurants,
                   'total_restaurants': total_resstaurants
                   }
    return render(request, 'food/restaurant.html', context)
