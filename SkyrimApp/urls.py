from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visualize/<str:form_type>/', views.visualize_data, name='visualize'),
]
