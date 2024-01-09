from rest_framework import generics, permissions
from .models import edu
from .serializers import eduSerializer
from django.shortcuts import render


class eduCreateView(generics.CreateAPIView):
    queryset = edu.objects.all()
    serializer_class = eduSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class eduListView(generics.ListAPIView):
    queryset = edu.objects.all()
    serializer_class = eduSerializer
    http_method_names = ['get']

class eduDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = edu.objects.all()
    serializer_class = eduSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'put', 'delete']

def edu_list_view(request):
    edu_list = edu.objects.all()
    return render(request, 'edu_list.html', {'edu_list': edu_list})