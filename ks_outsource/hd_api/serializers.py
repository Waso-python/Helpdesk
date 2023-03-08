from rest_framework import serializers
from helpdesk.models import Org, Appointment, User, TStatus, OrgUser, InfoSys, HelpType, Problem, Ticket, PhoneNumber

class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TStatus
        fields = '__all__'

class OrgUserSerializer(serializers.ModelSerializer):
    # user_appointment = AppointmentSerializer(many=False)
    # org = OrgSerializer(many=False)

    class Meta:
        model = OrgUser
        fields = '__all__'

class InfoSysSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoSys
        fields = '__all__'

class HelpTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpType
        fields = '__all__'

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer(many=False)
    status = TStatusSerializer(many=False)
    infosys = InfoSysSerializer(many=False)
    user = UserSerializer(many=False)
    help_type = HelpTypeSerializer(many=False)
    org_user = OrgUserSerializer(many=False)
    
    class Meta:
        model = Ticket
        fields = '__all__'

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id','phone','user']


