
from django.urls import include, path
from .views import vacancies, new

urlpatterns = [
    path('', vacancies),
    path('new', new)
]
