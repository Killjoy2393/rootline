from django.urls import path
from .views import home
from website.views import handle_contact_form_submission

urlpatterns = [
    path('', home, name='home'),  # главная, например
    path('handle-contact-form/', handle_contact_form_submission, name='handle_contact_form'),
]