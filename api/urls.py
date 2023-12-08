from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('sanctions/', views.getSanctions, name="sanctions"),
    path('sanctions/<str:pk>/update', views.updateSanction, name="update-sanction"),
    path('sanctions/<str:pk>/', views.getSanctionID, name="sanctionID"),
]