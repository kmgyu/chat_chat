from django.shortcuts import render, redirect
from ws_chat.models import ChatRoom

# Create your views here.
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "ws_chat/chatPage.html", context)

def chatLobby(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    
    # order by recently
    rooms = ChatRoom.objects.order_by("-created_at")
    return render(request, "ws_chat/chatLobby.html", {"rooms": rooms})
