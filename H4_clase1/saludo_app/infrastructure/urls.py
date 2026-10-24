from django.urls import path
from saludo_app.infrastructure.views import SaludoHttpAdapter

urlpatterns = [
    path('saludar/', SaludoHttpAdapter.as_view(), name='saludar'),
]