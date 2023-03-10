from rest_framework import serializers
from .models import User, Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['profile_number']


from rest_framework.generics import CreateAPIView
from .models import User, Customer
from .serializers import UserSerializer, CustomerSerializer

class CreateCustomerView(CreateAPIView):
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        # Get the user data from the request
        user_data = self.request.data.get('user')

        # Create a new user instance using the user serializer
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Create a new customer instance using the customer serializer
        serializer.save(user=user)

