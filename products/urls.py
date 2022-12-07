from django.urls import path
from products import views

urlpatterns = [
    path('', views.display_products),
    path('<int:pk>/', views.select_product)
]