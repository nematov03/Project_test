from django.urls import path
from .views import Index,DetailPage

urlpatterns = [
    path('',Index,name='index'),
    path('detail/<int:pk>',DetailPage,name = 'detail')
]
