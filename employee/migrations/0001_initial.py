# Generated by Django 3.0 on 2023-05-07 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_1_name', models.CharField(max_length=100, null=True)),
                ('company_1_designation', models.CharField(max_length=50, null=True)),
                ('company_1_salary', models.CharField(max_length=100, null=True)),
                ('company_1_duration', models.CharField(max_length=50, null=True)),
                ('company_2_name', models.CharField(max_length=100, null=True)),
                ('company_2_designation', models.CharField(max_length=50, null=True)),
                ('company_2_salary', models.CharField(max_length=100, null=True)),
                ('company_2_duration', models.CharField(max_length=50, null=True)),
                ('company_3_name', models.CharField(max_length=100, null=True)),
                ('company_3_designation', models.CharField(max_length=50, null=True)),
                ('company_3_salary', models.CharField(max_length=100, null=True)),
                ('company_3_duration', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Education_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_pg', models.CharField(max_length=50, null=True)),
                ('college_pg', models.CharField(max_length=100, null=True)),
                ('passing_year_pg', models.CharField(max_length=50, null=True)),
                ('percentage_pg', models.CharField(max_length=50, null=True)),
                ('course_g', models.CharField(max_length=50, null=True)),
                ('college_g', models.CharField(max_length=100, null=True)),
                ('passing_year_g', models.CharField(max_length=50, null=True)),
                ('percentage_g', models.CharField(max_length=50, null=True)),
                ('course_ss', models.CharField(max_length=50, null=True)),
                ('school_ss', models.CharField(max_length=100, null=True)),
                ('passing_year_ss', models.CharField(max_length=50, null=True)),
                ('percentage_ss', models.CharField(max_length=50, null=True)),
                ('school_hs', models.CharField(max_length=100, null=True)),
                ('passing_year_hs', models.CharField(max_length=50, null=True)),
                ('percentage_hs', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.CharField(max_length=50)),
                ('empdept', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('pcontact', models.CharField(max_length=15, null=True)),
                ('scontact', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('joiningdate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
