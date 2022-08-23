from cgitb import reset
import re
from django.contrib import admin
from django.db import models
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from .models import PhoneNumber, Ticket, Org, OrgUser, Problem, HelpType, InfoSys, TStatus, User, Appointment

#admin.site.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('dt', 'dt_plan', 'help_type', 'status', 'user', 'org_user', 'infosys', 'problem', 'comment')
admin.site.register(Ticket, TicketAdmin)

#admin.site.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'fullname', 'inn', 'on_contract')
admin.site.register(Org, OrgAdmin)

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone', 'user')
admin.site.register(PhoneNumber, PhoneAdmin)

#admin.site.register(OrgUser)
class OrgUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'sec_name', 'last_name', 'anydesk_id', 'user_appointment', 'org', 'get_phone', 'active')
    

admin.site.register(OrgUser, OrgUserAdmin)

#admin.site.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Problem, ProblemAdmin)

#admin.site.register(HelpType)
class HelpTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(HelpType, HelpTypeAdmin)

#admin.site.register(InfoSys)
class InfoSysAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment')
admin.site.register(InfoSys, InfoSysAdmin)

#admin.site.register(TStatus)
class TStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(TStatus, TStatusAdmin)

#admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'fullname', 'user_uid')
admin.site.register(User, UserAdmin)

#admin.site.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Appointment, AppointmentAdmin)



# Register your models here.
