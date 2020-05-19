from django.urls import path
from customuser import views

urlpatterns = [
    path('home/', views.index, name='homepage'),
    path('', views.login_request, name='login'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request),
    path('signup/', views.signup)
]
