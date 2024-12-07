from django.urls import path , include
from . import views 

urlpatterns = [
    path('' , views.registerUser , name = 'register'),
    path('login/' , views.loginUser , name = 'login'),
    path('userinterface/', include('userInterface.urls')),
    path('logout/' , views.logoutUser , name = 'logout'),
]
