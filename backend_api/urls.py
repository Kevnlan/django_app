from urllib.parse import urlparse
from django.urls import path
from django.contrib import admin
#now import the views.py file into this code
from . import views
from .views import EmployeesViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('employees', EmployeesViewSet, basename='employees')	

urlpatterns = router.urls