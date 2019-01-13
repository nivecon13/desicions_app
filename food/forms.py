import datetime
from django import forms

from .choices import *

class RestaurantForm(forms.Form):
    restaurant_name_text = forms.CharField(label="Restaurant name", max_length=50, required=False)
    restaurant_city_text = forms.CharField(label="City", max_length=50, required=False)
    restaurant_type_text = forms.CharField(label="Cuisine", max_length=50, required=False)
    what_we_ate_text = forms.CharField(label="What did we eat?", max_length=250, required=False)
    when_we_ate_text = forms.DateField(initial=datetime.date.today)
    meal_cost_text = forms.FloatField(min_value=0, label="How much did it cost?")
    rating_coly_text = forms.ChoiceField(choices=[("", "Coly's rating")] + rating_choices)
    rating_michael_text = forms.ChoiceField(choices=[("", "Michael's rating")] + rating_choices)
    would_come_again_text = forms.ChoiceField(choices=[("", "Would we come again?")] + come_again_choices)