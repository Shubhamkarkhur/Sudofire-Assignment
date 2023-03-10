# Step one
Define the serializers for the user and customer models. You can use the ModelSerializer class provided by Django REST Framework to automatically generate the serializers based on the model fields.
# step Two
Define the view for creating a customer. You can use the CreateAPIView class provided by Django REST Framework to handle the creation of a new customer instance.
# step Three
from django.urls import path
from .views import CreateCustomerView



