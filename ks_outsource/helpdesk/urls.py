from django.urls import path
from .views import OrgUserCreate, JSONListView,  TicketListView, OrgUserDetailView



from . import views

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket_list'),
    path('orguser/', JSONListView.as_view(), name='orguser_list'),
    path('neworguser/', OrgUserCreate.as_view(), name='orgusernew'),
    path('orguser/<int:id>/', OrgUserDetailView.as_view(), name='orguser_detail'),
    
]