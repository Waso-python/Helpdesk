from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hd_api import views
from .views import OrgViewSet, AppointmentViewSet, UserViewSet, TStatusViewSet, OrgUserViewSet, InfoSysViewSet, HelpTypeViewSet, ProblemViewSet, TicketViewSet, PhoneNumberViewSet

router = DefaultRouter()
router.register(r'org', OrgViewSet, basename='org')
router.register(r'appointment', AppointmentViewSet, basename='appointment')
router.register(r'user', UserViewSet, basename='user')
router.register(r'tstatus', TStatusViewSet, basename='tstatus')
router.register(r'orguser', OrgUserViewSet, basename='orguser')
router.register(r'infosys', InfoSysViewSet, basename='infosys')
router.register(r'helptype', HelpTypeViewSet, basename='helptype')
router.register(r'problem', ProblemViewSet, basename='problem')
router.register(r'ticket', TicketViewSet, basename='ticket')
router.register(r'phonenumber', PhoneNumberViewSet, basename='phonenumber')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('orgs/', views.OrgList.as_view(), name='org_list'),
#     path('orgs/<int:pk>/', views.OrgDetail.as_view(), name='org_detail'),
#     path('appointments/', views.AppointmentList.as_view(), name='appointment_list'),
#     path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment_detail'),
#     path('users/', views.UserList.as_view(), name='user_list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
#     path('tstatus/', views.TStatusList.as_view(), name='tstatus_list'),
#     path('tstatus/<int:pk>/', views.TStatusDetail.as_view(), name='tstatus_detail'),
#     path('orgusers/', views.OrgUserList.as_view(), name='orguser_list'),
#     path('orgusers/<int:pk>/', views.OrgUserDetail.as_view(), name='orguser_detail'),
#     path('infosys/', views.InfoSysList.as_view(), name='infosys_list'),
#     path('infosys/<int:pk>/', views.InfoSysDetail.as_view(), name='infosys_detail'),
#     path('helptypes/', views.HelpTypeList.as_view(), name='helptype_list'),
#     path('helptypes/<int:pk>/', views.HelpTypeDetail.as_view(), name='helptype_detail'),
#     path('problems/', views.ProblemList.as_view(), name='problem_list'),
#     path('problems/<int:pk>/', views.ProblemDetail.as_view(), name='problem_detail'),
#     path('tickets/', views.TicketList.as_view(), name='ticket_list'),
#     path('tickets/<int:pk>/', views.TicketDetail.as_view(), name='ticket_detail'),
#     path('phonenumbers/', views.PhoneNumberList.as_view(), name='phonenumber_list'),
#     path('phonenumbers/<int:pk>/', views.PhoneNumberDetail.as_view(), name='phonenumber_detail'),
# ]

