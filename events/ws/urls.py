from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from ws import views as chat_views

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),
   
    # для ws
    path("auth/login/", LoginView.as_view
         (template_name="ws/loginpage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
