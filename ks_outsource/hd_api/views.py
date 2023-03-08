from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from helpdesk.models import Org, Appointment, User, TStatus, OrgUser, InfoSys, HelpType, Problem, Ticket, PhoneNumber
from .serializers import OrgSerializer, AppointmentSerializer, UserSerializer, TStatusSerializer, OrgUserSerializer, InfoSysSerializer, HelpTypeSerializer, ProblemSerializer, TicketSerializer, PhoneNumberSerializer
from rest_framework.pagination import PageNumberPagination

class OrgViewSet(viewsets.ModelViewSet):
    queryset = Org.objects.all()
    serializer_class = OrgSerializer
    permission_classes = [IsAuthenticated]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class TStatusViewSet(viewsets.ModelViewSet):
    queryset = TStatus.objects.all()
    serializer_class = TStatusSerializer
    permission_classes = [IsAuthenticated]


class OrgUserViewSet(viewsets.ModelViewSet):
    queryset = OrgUser.objects.all()
    serializer_class = OrgUserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class InfoSysViewSet(viewsets.ModelViewSet):
    queryset = InfoSys.objects.all()
    serializer_class = InfoSysSerializer
    permission_classes = [IsAuthenticated]


class HelpTypeViewSet(viewsets.ModelViewSet):
    queryset = HelpType.objects.all()
    print(queryset)
    serializer_class = HelpTypeSerializer
    permission_classes = [IsAuthenticated]


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    permission_classes = [IsAuthenticated]

# class OrgList(generics.ListCreateAPIView):
#     queryset = Org.objects.all()
#     serializer_class = OrgSerializer
#     permission_classes = [IsAuthenticated]

# class OrgDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Org.objects.all()
#     serializer_class = OrgSerializer
#     permission_classes = [IsAuthenticated]
    
# class AppointmentList(generics.ListCreateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
#     permission_classes = [IsAuthenticated]

# class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
    
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class TStatusList(generics.ListCreateAPIView):
#     queryset = TStatus.objects.all()
#     serializer_class = TStatusSerializer

# class TStatusDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TStatus.objects.all()
#     serializer_class = TStatusSerializer
    
# class OrgUserList(generics.ListCreateAPIView):
#     queryset = OrgUser.objects.all()
#     serializer_class = OrgUserSerializer

# class OrgUserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = OrgUser.objects.all()
#     serializer_class = OrgUserSerializer
    
# class InfoSysList(generics.ListCreateAPIView):
#     queryset = InfoSys.objects.all()
#     serializer_class = InfoSysSerializer

# class InfoSysDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = InfoSys.objects.all()
#     serializer_class = InfoSysSerializer
    
# class HelpTypeList(generics.ListCreateAPIView):
#     queryset = HelpType.objects.all()
#     serializer_class = HelpTypeSerializer

# class HelpTypeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HelpType.objects.all()
#     serializer_class = HelpTypeSerializer
    
# class ProblemList(generics.ListCreateAPIView):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemSerializer

# class ProblemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemSerializer
    
# class TicketList(generics.ListCreateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     pagination_class = PageNumberPagination

# class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     pagination_class = PageNumberPagination

# class PhoneNumberList(generics.ListCreateAPIView):
#     queryset = PhoneNumber.objects.all()
#     serializer_class = PhoneNumberSerializer
#     pagination_class = PageNumberPagination

# class PhoneNumberDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PhoneNumber.objects.all()
#     serializer_class = PhoneNumberSerializer
#     pagination_class = PageNumberPagination