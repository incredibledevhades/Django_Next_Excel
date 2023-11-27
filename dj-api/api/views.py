# api/views.py
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from django.http import JsonResponse
from django.middleware import csrf


def apiOverview(request):
    return JsonResponse("API Base point", safe=False)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# def UserRegister(generics.CreateAPIView):
#     return JsonResponse([{
#         'user': {
#             'id': '1',
#             'userName': 'alex',
#             'gender': 'male',
#             'email': 'alexjohnny.business@gmail.com'
#         },
#         'accessToken': 'aaa'
#     }], safe=False)

class UserRegister(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



def GetCsrfToken(request):
    # Get the CSRF token using csrf.get_token
    csrf_token = csrf.get_token(request)

    # Include the CSRF token in the response
    response_data = {'csrfToken': csrf_token}
    return JsonResponse(response_data)