from rest_framework import routers
from django.urls import path, include
from todos.views import FacebookLogin, GoogleLogin, TodoViewSet


router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todos')


urlpatterns = [
    path('', include(router.urls)),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
]