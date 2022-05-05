# Generated by Django 4.0.4 on 2022-05-05 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('frname', models.CharField(default='', max_length=30)),
                ('birthday', models.CharField(default='', max_length=20)),
                ('address1', models.CharField(default='', max_length=50)),
                ('address2', models.CharField(default='', max_length=50)),
                ('code', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=30)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]