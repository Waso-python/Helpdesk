from django_filters import rest_framework as filters
from helpdesk.models import OrgUser, PhoneNumber, Org

class OrgUserFilter(filters.FilterSet):
    class Meta:
        model = OrgUser
        fields = {
            'org__id': ['exact'],
            
        }
