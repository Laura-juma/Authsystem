from django.urls import path
from .views import SignUpView, CustomLoginView, login_success
from django.contrib.auth.views import LogoutView

urlpatterns=[
  path('signup/',SignUpView.as_view(), name='signup'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('login-success/', login_success, name='login_success'),
  path('logout/', LogoutView.as_view(), name='logout'),

]