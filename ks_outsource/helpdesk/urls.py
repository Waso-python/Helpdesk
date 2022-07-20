from django.urls import path
from .views import OrgUserCreate, ContactView, JSONListView, JSONDetailView, JSONUpdate, JSONDelete, TicketListView



from . import views

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket_list'),
    path('orguserDetail/<int:pk>/', JSONDetailView.as_view(), name='orguser-detail'),
    path('orguserUpdate/<int:pk>/', JSONUpdate.as_view(), name='orguser-update'),
    path('orguserDelete/<int:pk>/', JSONDelete.as_view(), name='orguser-delete'),
    path('orguser/', JSONListView.as_view(), name='orguser_list'),
    path('neworguser/', OrgUserCreate.as_view(), name='orgusernew'),
]