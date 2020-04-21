"""FoodPantry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from checkout import views as checkout_views
from dashboard import views as dashboard_views
from impact_measurement import views as impact_measurement_views
from inventory import views as inventory_views
from provider import views as provider_views
from waste_reduction import views as waste_reduction_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_views.dashboard, name='dashboard'),
    path('checkout/', checkout_views.checkout, name='checkout'),
    path('impact/', impact_measurement_views.impact_measurement, name='impact'),
    path('inventory/', inventory_views.inventory, name='inventory'),
    path('provider/', provider_views.provider, name='provider'),
    path('waste/', waste_reduction_views.waste_reduction, name='waste')
]
