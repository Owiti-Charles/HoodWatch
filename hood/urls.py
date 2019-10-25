from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.SignupForm, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
]
