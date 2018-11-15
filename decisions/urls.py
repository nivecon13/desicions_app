from django.urls import path

from . import views

#this tells django templates what url to use if other apps have same url names
app_name = 'decisions'

urlpatterns = [
    path('choices', views.get_choices, name='choices'),
    path('decisions', views.DesicionsView, name='decisions'),
    path('all', views.DecisionsAll, name='all'),
    path('<int:pk>/result', views.ResultsView.as_view(), name='result')
]