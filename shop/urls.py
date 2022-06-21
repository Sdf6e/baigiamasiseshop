from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.mainscreen),
    path('products/<int:id>/', views.product_detail),
    path('products/', views.product_list)
]
