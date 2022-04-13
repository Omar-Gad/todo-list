from turtle import title
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


from rest_framework import viewsets, status
from rest_framework.response import Response

from todos import models, serializers, permissions

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TodoSerializer
    queryset = models.Todo.objects.all()
    permission_classes = (permissions.IsAuthorOrReadOnly,)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            models.Todo.objects.create(
                title=serializer.validated_data['title'],
                active=serializer.validated_data['active'],
                user=request.user,
                )
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            
            
    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            todo = models.Todo.objects.get(pk=pk)
            todo.title = serializer.validated_data['title']
            todo.active = serializer.validated_data['active']
            todo.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    
            
    def destroy(self, request, pk=None):
        models.Todo.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
            

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/accounts/google/login/callback/"
    client_class = OAuth2Client
    
