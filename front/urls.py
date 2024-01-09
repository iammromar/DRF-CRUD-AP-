from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.eduListView.as_view(), name='message-list'),
    path('api/create/', views.eduCreateView.as_view(), name='message-create'),
    path('api/<int:pk>/', views.eduDetailView.as_view(), name='edu-detail'),
    
    path('educations/', views.edu_list_view, name='edu-list-view'),  # Yeni eklenen URL
]