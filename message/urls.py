from django.urls import path, include
from .views import TreadListView, ThreadDetailView, add_message, start_thread

message_patterns = ([
    path('', TreadListView.as_view(), name="list"),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name="detail"),
    path('thread/<int:pk>/add/', add_message, name="add"),
    path('thread/start/<username>/', start_thread, name="start"),
], "messenger")