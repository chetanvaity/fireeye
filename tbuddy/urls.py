from django.urls import path, include

from . import views

app_name = 'tbuddy'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('listt', views.listt, name='listt'),
    path('travel/add', views.addTravel, name='addTravel'),
    path('travel/<int:pk>/', views.showTravelView.as_view(), name='showTravel'),
    path('travel/search', views.searchTravel, name='searchTravel')
]
