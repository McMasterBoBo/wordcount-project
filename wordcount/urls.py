
from django.urls import path
from . import views

# You can change your own web name by changing the 'admin/'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
]
