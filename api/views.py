from store.models import Category, Product
from account.models import UserBase
from store.serializers import CategorySerializers, ProductSerializer
from account.serializers import UserSerializer, UserRegistrationSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

class CategoryList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class UserRegisteration(generics.CreateAPIView):
    queryset = UserBase.objects.all()
    serializer_class= UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)

            return Response({
                'response': 'Account has been created',
                'user_name': user.user_name,
                'email': user.email,
                'token': token.key
            }, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['POST'])
# def user_register_view(request):
#     if request.method == 'POST':
#         serializer = UserRegistrationSerializer(data=request.data)

#         data = {}

#         if serializer.is_valid():
#             account = serializer.save()

#             data['response'] = 'Account has been created'
#             data['user_name'] = account.user_name
#             data['email'] = account.email

#             token = Token.objects.get(user=account).key
#             data['token'] = token

#             return Response(data, status=status.HTTP_201_CREATED)

#         else:
#             data = serializer.errors 

#             return Response(data, status=status.HTTP_400_BAD_REQUEST)
