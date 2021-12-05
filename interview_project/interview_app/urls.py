from django.urls import path 
from . import views

urlpatterns = [
    path('<int:physicalport_id>/', views.physicalport, name="physicalport"),
    path('<int:physicalport_id>/users', views.users, name="users")
]