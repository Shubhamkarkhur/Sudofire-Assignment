urlpatterns = [
    path('customers/create/', CreateCustomerView.as_view(), name='create-customer'),
]