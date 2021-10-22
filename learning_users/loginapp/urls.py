from django.urls import path
from loginapp.views import register,user_login

app_name = "loginapp"

urlpatterns = [
    path('', register, name="register"),
    path('login/', user_login, name = "user_login")

]
