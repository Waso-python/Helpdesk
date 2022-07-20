# Generated by Django 4.0.6 on 2022-07-19 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0010_alter_orguser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orguser',
            name='phone',
            field=models.CharField(max_length=100, null=True, verbose_name='Телефоны'),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helpdesk.orguser')),
            ],
        ),
    ]