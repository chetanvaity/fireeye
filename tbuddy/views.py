from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from tbuddy.models import Travel, TravelForm, SearchForm

def listt(request):
    travel_list = Travel.objects.all()
    context = {'travel_list': travel_list}
    return render(request, 'tbuddy/travel_list.html', context)


def addTravel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.save()
            return HttpResponseRedirect(reverse('tbuddy:listt'))
    else:
        form = TravelForm()
        return render(request, 'tbuddy/travel.html', {'form': form})
    
    return render(request, 'tbuddy/travel.html', {'form': form})


class showTravelView(generic.DetailView):
    model = Travel
    template_name = 'tbuddy/showTravel.html'


def searchTravel(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Retreive proper tList based on query
            tlist = Travel.objects.filter(destination__startswith=form.cleaned_data['query'])
            return render(request, 'tbuddy/searchResults.html', {'form': form, 'tlist': tlist})

    form = SearchForm()
    return render(request, 'tbuddy/search.html', {'form': form})
    
