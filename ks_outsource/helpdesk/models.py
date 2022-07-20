from unicodedata import name
from xml.etree.ElementTree import Comment
from django.db import models
from django.utils import timezone


# Create your models here.
class Org(models.Model):
    name = models.CharField(max_length=255, verbose_name='Короткое наименование')
    fullname = models.TextField(verbose_name='Полное наименование', null=True,blank=True)
    inn = models.CharField(max_length=13, verbose_name='ИНН', null=True,blank=True)
    on_contract = models.BooleanField(verbose_name='контракт заключен', default=True)

    def __str__(self) -> str:
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Должность')

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Username', null=False)
    fullname = models.CharField(max_length=100, verbose_name='name', blank=True)
    user_uid = models.UUIDField(null=True,blank=True)

    def __str__(self) -> str:
        return self.fullname

class TStatus(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Статус задачи')

    def __str__(self) -> str:
        return self.name


class OrgUser(models.Model):
    first_name = models.CharField(max_length=100, null=False, verbose_name='Имя')
    sec_name = models.CharField(max_length=100, null=True, verbose_name='Отчество',blank=True)
    last_name = models.CharField(max_length=100, null=True, verbose_name='Фамилия',blank=True)
    phone = models.CharField(max_length=100, null=True, verbose_name='Телефоны')
    anydesk_id = models.CharField(max_length=50, verbose_name= 'ID AnyDesk', null=True,blank=True)
    user_appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT, null=True)
    org = models.ForeignKey(Org, on_delete=models.PROTECT)

    def get_phone(self):
        result = PhoneNumber.objects.filter(user = self).values_list('phone')
        res = ''
        for i in result:
            k = 0
            for value in i:
                res = res + (', ' if res else ' ')+ value 
                
        return res
    
    # def add_phone(self, obj):
    #     PhoneNumber.

    def __str__(self) -> str:
        return self.first_name+' '+(self.sec_name if self.sec_name else '') + ' '+ self.user_appointment.name + self.org.name

class PhoneNumber(models.Model):
    phone = models.CharField(max_length=15, blank=True)
    user = models.ForeignKey(OrgUser, on_delete=models.PROTECT)


class InfoSys(models.Model):
    name = models.CharField(max_length=250, null=False, verbose_name='Инф. система')
    comment = models.TextField(verbose_name='Комментарий',blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class HelpType(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Тип связи')

    def __str__(self) -> str:
        return self.name

class Problem(models.Model):
    name = models.CharField(max_length=250, verbose_name='Проблема')
    infosys = models.ManyToManyField(InfoSys)

    def __str__(self) -> str:
        return self.name

class Ticket(models.Model):
    
    dt = models.DateField(default=timezone.now)
    dt_plan = models.DateField(verbose_name='Дата повторной связи', null=True, blank=True)
    help_type = models.ForeignKey(HelpType, on_delete=models.PROTECT)
    status = models.ForeignKey(TStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    org_user = models.ForeignKey(OrgUser, on_delete=models.PROTECT)
    infosys = models.ForeignKey(InfoSys, on_delete=models.PROTECT)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    comment = models.TextField(verbose_name='Комментарий', null=True,blank=True)

    def __str__(self):
        return str(self.dt)+' '+self.status.name+' '+self.infosys.name+' '+self.problem.name + ' ' + self.org_user.org.name

"""Закончить главную модель и определить методы"""