from django.urls import path, include
from ws_chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", chat_views.chatLobby, name='chat-lobby'),
    path("chat/<str:room_name>/", chat_views.chatPage, name="chat-page"),

    # login-section
    path("auth/login/", LoginView.as_view(template_name="ws_chat/loginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
