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
        
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self) -> str:
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Должность')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Username', null=False)
    fullname = models.CharField(max_length=100, verbose_name='name', blank=True)
    user_uid = models.UUIDField(null=True,blank=True)

    def __str__(self) -> str:
        return self.fullname

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class TStatus(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Статус задачи')

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class OrgUser(models.Model):
    first_name = models.CharField(max_length=100, null=False, verbose_name='Имя')
    sec_name = models.CharField(max_length=100, null=True, verbose_name='Отчество',blank=True)
    last_name = models.CharField(max_length=100, null=True, verbose_name='Фамилия',blank=True)
    phone = models.CharField(max_length=100, null=True, verbose_name='Телефоны',blank=True)
    anydesk_id = models.CharField(max_length=50, verbose_name= 'ID AnyDesk', null=True,blank=True)
    user_appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, verbose_name= 'Должность')
    org = models.ForeignKey(Org, on_delete=models.CASCADE, verbose_name= 'Организация')
    active = models.BooleanField(verbose_name='Активен', default=True)


    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ['org__name', 'last_name']

    def get_phone(self):
        self.phone_optimize()
        result = PhoneNumber.objects.filter(user = self).values_list('phone')
        res = ''
        for i in result:
            k = 0
            for value in i:
                res = res + (', ' if res else ' ')+ value 
        return res

    def phone_optimize(self):
        def save_phone(phone:str):
            print(phone)
            phone = phone.strip()
            if PhoneNumber.objects.filter(user = self, phone = phone).count() == 0:
                ph = PhoneNumber(user = self, phone = phone)
                ph.save()
            
        if self.phone:
            phone_list = self.phone.strip().replace('+','').replace('-','').split(',')
            for el in phone_list:
                if el:
                    res_str = ''
                    for c in el:
                        if c.isdigit():
                            res_str = res_str + str(c)
                    save_phone('+7' + res_str[1:])
            self.phone = ''
            self.save()
       


    def __str__(self) -> str:
        return f"{self.first_name} {self.sec_name} {self.last_name} {self.org.name}"

class PhoneNumber(models.Model):
    phone = models.CharField(max_length=15, blank=True)
    user = models.ForeignKey(OrgUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"


class InfoSys(models.Model):
    name = models.CharField(max_length=250, null=False, verbose_name='Инф. система')
    comment = models.TextField(verbose_name='Комментарий',blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "ИС"
        verbose_name_plural = "ИС"

class HelpType(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Тип связи')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Тип поддержки"
        verbose_name_plural = "Типы поддержки"

class Problem(models.Model):
    name = models.CharField(max_length=250, verbose_name='Проблема')
    # infosys = models.ManyToManyField(InfoSys)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Проблема"
        verbose_name_plural = "Список проблем"

class Ticket(models.Model):
    
    dt = models.DateField(default=timezone.now)
    dt_plan = models.DateField(verbose_name='Дата повторной связи', null=True, blank=True)
    help_type = models.ForeignKey(HelpType, on_delete=models.CASCADE)
    status = models.ForeignKey(TStatus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org_user = models.ForeignKey(OrgUser, on_delete=models.CASCADE)
    infosys = models.ForeignKey(InfoSys, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий', null=True,blank=True)

    def __str__(self):
        return str(self.dt)+' '+self.status.name+' '+self.infosys.name+' '+self.problem.name + ' ' + self.org_user.org.name

    def get_forward_date(self):
        return True if self.dt_plan else False

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"


"""Закончить главную модель и определить методы"""