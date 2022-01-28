from django.urls import path
from main import views

urlpatterns=[
    path("products/add",views.CreateProduct.as_view(),name="addproduct")
]
