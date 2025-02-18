from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),  # Страница со всеми услугами
    path('<slug:slug>/', views.service_detail, name='service_detail'),  # Страница конкретной услуги
]
