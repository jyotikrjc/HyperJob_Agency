from django.urls import include, path
from .views import resumes, new

urlpatterns = [
    path('', resumes),
    path('new', new)
]
