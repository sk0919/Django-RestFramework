from rest_framework import generics , mixins
from .serializers import  UserSerializer
from .models import Consumer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
class UserDetailView(generics.RetrieveAPIView):
    queryset = Consumer.objects.all()
    serializer_class = UserSerializer
    
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Consumer.objects.all()
    serializer_class = UserSerializer    
    
class UsersListView(generics.ListAPIView):
    queryset = Consumer.objects.all()
    serializer_class = UserSerializer
    
class UserDeleteView(generics.DestroyAPIView):
    queryset = Consumer.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""
#function based views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizers import UserSerializer
from .models import *
from .serilizers import UserSerializer

#function based views for creating the users
@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"}) 
    else:
        data = {
          "error": True,
          "errors": serializer.errors,          
        }
        return Response(data)   
        
#function based views for showing details of the users
@api_view(["GET"])
def user_details(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
    
#function based views for updating details of the users
@api_view(["GET", "PUT"])
def user_update(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors, "error": True}) 
    serializer = UserSerializer(user)
    return Response(serializer.data)
    
#function based views for showing every users
@api_view(["GET"])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

#function based views for deleting users
def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return Response({"message": "Deleted"})
"""


    
