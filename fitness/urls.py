from django.urls import path
from .views import Login, SignUp, Index,outdoor,Indoor,timing,register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Index.as_view(), name='indexpage'),
    path('login', Login.as_view(), name='login'),
    path('signup', SignUp.as_view(), name='signup'),
    path('outdoor',outdoor.as_view(),name='outdoor'),
    path('Indoor',Indoor.as_view(),name='Indoor'),
    path('timing',timing.as_view(),name='timing'),
    path('register',register.as_view(),name='register'),
]