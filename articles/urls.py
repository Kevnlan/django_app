from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
]