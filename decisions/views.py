from random import random

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Decision
from .forms import DecisionForm

def get_choices(request):
    if request.method == 'POST':
        form = DecisionForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            d = Decision(
                username=form.cleaned_data['username_text'],
                question=form.cleaned_data['question_text'],
                option_1=form.cleaned_data['option_1_text'],
                option_2=form.cleaned_data['option_2_text'],
                decision_made=round(random()+1),
                pub_date=timezone.now()
                )
            d.save()
            return HttpResponseRedirect(reverse('decisions:result', args=(d.id,)))
    else:
        form = DecisionForm()
    return render(request, 'decisions/choices.html', {'form': form})

class ResultsView(generic.DetailView):
    model = Decision
    template_name = 'decisions/result.html'
    context_object_name = 'decision'

def DesicionsView(request):
    latest_decisions_list = Decision.objects.order_by('-pub_date')[:5]
    return render(request, 'decisions/decisions.html', {'latest_decisions_list': latest_decisions_list})

def DecisionsAll(request):
    decision_list = Decision.objects.all()
    paginator = Paginator(decision_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    decisions = paginator.get_page(page)
    return render(request, 'decisions/list.html', {'decisions': decisions})