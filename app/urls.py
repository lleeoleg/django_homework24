from django.urls import path
from .views import FilmsListView


urlpatterns = [
    path('list/', FilmsListView.as_view(), name='films_list'),
]
