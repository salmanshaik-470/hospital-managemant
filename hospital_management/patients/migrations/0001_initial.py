# Generated by Django 3.2.6 on 2021-08-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientSubmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('location', models.CharField(choices=[('hyderabad', 'hyderabad'), ('guntur', 'guntur'), ('vijayawada', 'vijayawada')], default='1', max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='1', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('Appointment_date', models.DateField(verbose_name=True)),
            ],
        ),
    ]