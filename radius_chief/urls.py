from django.urls import path
from . import views

urlpatterns = [
    path('radpostauth/', views.RadPostAuthListView.as_view()),
    path('radcheck/', views.RadCheckListCreateView.as_view()),
    path('radcheck/<pk>', views.RadCheckUpdateDestroyView.as_view()),
    path('radusergroup/', views.RadUserGroupListCreateView.as_view()),
    path('radusergroup/<pk>', views.RadUserGroupUpdateDestroyCreateView.as_view())
]
