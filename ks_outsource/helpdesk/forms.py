from django import forms
from .models import OrgUser, Org

class OrgUserForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sec_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    org = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}))
    phones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = OrgUser
        fields = ('first_name', 'sec_name', 'last_name',  "org", "phones")
        
        