from django.urls import path, include
from ws_chat.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    path("chat/<str:room_name>/" , ChatConsumer.as_asgi()) , 
] 
# regex 사용 시 예제. (반드시 re_path를 이용해야 한다!)
# re_path(r"chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi())
# (?P<room_name>...) : room_name이 이름이 되는 그룹을 만든다. (django에서 kwargs로 전달 가능)
# \w+ : 하나 이상의 단어 문자를 포함해야 함.
# /$ : URL이 반드시 /로 끝나야 한다.
