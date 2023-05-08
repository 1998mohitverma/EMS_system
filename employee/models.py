from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    pcontact = models.CharField(max_length=15, null=True)
    scontact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    joiningdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username

class Employee_Education_history(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_pg = models.CharField(max_length=50, null=True)
    college_pg = models.CharField(max_length=100,null=True)
    passing_year_pg = models.CharField(max_length=50,null=True)
    percentage_pg = models.CharField(max_length=50,null=True)

    course_g = models.CharField(max_length=50, null=True)
    college_g = models.CharField(max_length=100,null=True)
    passing_year_g = models.CharField(max_length=50,null=True)
    percentage_g = models.CharField(max_length=50,null=True)

    course_ss = models.CharField(max_length=50, null=True)
    school_ss = models.CharField(max_length=100,null=True)
    passing_year_ss = models.CharField(max_length=50,null=True)
    percentage_ss = models.CharField(max_length=50,null=True)

    school_hs = models.CharField(max_length=100,null=True)
    passing_year_hs = models.CharField(max_length=50,null=True)
    percentage_hs = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.user.username

class Employee_Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_1_name = models.CharField(max_length=100,null=True)
    company_1_designation = models.CharField(max_length=50,null=True)
    company_1_salary = models.CharField(max_length=100,null=True)
    company_1_duration = models.CharField(max_length=50,null=True)

    company_2_name = models.CharField(max_length=100,null=True)
    company_2_designation = models.CharField(max_length=50,null=True)
    company_2_salary = models.CharField(max_length=100,null=True)
    company_2_duration = models.CharField(max_length=50,null=True)

    company_3_name = models.CharField(max_length=100,null=True)
    company_3_designation = models.CharField(max_length=50,null=True)
    company_3_salary = models.CharField(max_length=100,null=True)
    company_3_duration = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.user.username