from django import forms
from django_json_widget.widgets import JSONEditorWidget
from .models import OrgUser

class OrgUserForm(forms.ModelForm):

    class Meta:
        model = OrgUser
        fields = ('first_name', 'sec_name', 'last_name', "phone", "org",)
        widgets = {
            'phone': JSONEditorWidget
        }