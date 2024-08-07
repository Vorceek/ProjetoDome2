from django.urls import path
from .views import export_to_excel, index

urlpatterns = [
    path('', index, name='index'),
    path('export_to_excel/', export_to_excel, name='export_to_excel'),
]
