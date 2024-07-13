from django.urls import path
from .views import JsonFormatView

urlpatterns = [
    path('format-json/', JsonFormatView.as_view(), name='format-json'),
]
