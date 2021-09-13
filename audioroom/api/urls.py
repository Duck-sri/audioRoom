from django.urls import path
from .views import main
from .views import RoomView,RoomPost

urlpatterns = [
		path('',main),
		path('view/',RoomView.as_view()),
		path('post/',RoomPost.as_view())
]
