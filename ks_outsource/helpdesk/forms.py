from django import forms
from .models import OrgUser, Org

class OrgUserForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),strip=True, required=True)
    sec_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),strip=True, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),strip=True, required=False)
    org = forms.ModelChoiceField(queryset=Org.objects.all(),  widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    phones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)


    class Meta:
        model = OrgUser
        fields = ('first_name', 'sec_name', 'last_name',  "org", "phones")
        
        