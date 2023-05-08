from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def registration_page(request):
    if request.method == 'POST':
        error = ""
        fname = request.POST['fname']
        lname = request.POST['lname']
        empcode = request.POST['empcode']
        email = request.POST['email']
        pwd = request.POST['pwd']
        # c_pwd = request.POST['cpwd']
        try:
            user = User.objects.create_user(first_name=fname,last_name=lname,username=email,password=pwd)
            Employee_Details.objects.create(user=user,empcode=empcode)
            Employee_Experience.objects.create(user=user)
            Employee_Education_history.objects.create(user=user)
            print("employee registration successfully insert !!")
            error="no"
        except:
            error="yes"

    return render(request, 'registration.html', locals())

def emp_login(request):
    error="no"
    if request.method == 'POST':
        uname = request.POST['email']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)
        print(f"user : {user}")
        if user is not None:
            login(request,user)
            print("Employee login successfully and redirect to dashboard page.")
            return redirect('home_page')
        else:
            msg = "Your Credentials are wrong!! Please Enter Correct Details"
            return render(request, 'emp_login.html',{'msg':msg})    
    else:
        return render(request, 'emp_login.html')

def home_page(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')

def emp_profile(request):
    user = request.user
    employee = Employee_Details.objects.get(user=user)
    print(f"current user is : {employee}")
    if request.method == 'POST':
        error = ""
        fname = request.POST['fname']
        lname = request.POST['lname']
        empcode = request.POST['empcode']
        email = request.POST['email']
        empdept = request.POST['department']
        designation = request.POST['designation']
        pcontact = request.POST['pcontact']
        scontact = request.POST['scontact']
        gender = request.POST['gender']
        jdate = request.POST['jdate']

        employee.user.first_name = fname
        employee.user.last_name = lname
        employee.user.username = email
        employee.empcode = empcode
        employee.empdept = empdept
        employee.designation = designation
        employee.pcontact = pcontact
        employee.scontact = scontact
        employee.gender = gender
        if jdate:
            employee.joiningdate = jdate
        print(f"Current employe == {employee}")    
        # c_pwd = request.POST['cpwd']
        try:
            employee.save()
            employee.user.save()
            print("employee profile updated successfully")
            error="no"
        except:
            error="yes"
    return render(request, 'emp_profile.html',{'employee':employee})

def emp_logout(request):
    logout(request)
    return redirect('emp_login')

def admin_login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=uname, password=password)
        print(f"user is : {user}")
        try:
            if user.is_staff:
                login(request,user)
                return redirect('admin_dashboard')
        except:
            print("something went wrong !! Please trye again")            
    return render(request, 'admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin_all_employees(request):
    employees = Employee_Details.objects.all()
    print(f"Employee = {employees}")
    return render(request, 'admin_all_employees.html',{'employees':employees})

def admin_change_password(request):
    user = request.user
    print(f"current user == {user}")
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password!=confirm_password:
            print("both password didn't match ! Please try again")
        else:
            try:
                if user.check_password(current_password):
                    user.set_password(new_password)
                    print("password is available")
                    user.save()
                    print("password is set successfully")
                else:
                    print("password is not available")    
            except:
                error = "yes"
                print(f"Error occured !! {error}")
    return render(request, 'admin_change_password.html')

def emp_experience(request):
    if not request.user.is_authenticated:
        return render('emp_login')
    user = request.user
    exp = Employee_Experience.objects.get(user=user)
    print(f"Emp Experience : {exp}")
    return render(request, 'emp_exp.html',{'experience':exp})

def edit_experience(request):
    if not request.user.is_authenticated:
        return render('emp_login')
    user = request.user
    exp = Employee_Experience.objects.get(user=user)
    if request.method == 'POST':
        cmp_1_name = request.POST['company_1_name']
        cmp_1_designation = request.POST['company_1_designation']
        cmp_1_salary = request.POST['company_1_salary']
        cmp_1_duration = request.POST['company_1_duration']

        cmp_2_name = request.POST['company_2_name']
        cmp_2_designation = request.POST['company_2_designation']
        cmp_2_salary = request.POST['company_2_salary']
        cmp_2_duration = request.POST['company_2_duration']

        cmp_3_name = request.POST['company_3_name']
        cmp_3_designation = request.POST['company_3_designation']
        cmp_3_salary = request.POST['company_3_salary']
        cmp_3_duration = request.POST['company_3_duration']

        # Insert data in Experience table:
        exp.company_1_name = cmp_1_name
        exp.company_1_designation = cmp_1_designation
        exp.company_1_salary = cmp_1_salary
        exp.company_1_duration = cmp_1_duration

        exp.company_2_name = cmp_2_name
        exp.company_2_designation = cmp_2_designation
        exp.company_2_salary = cmp_2_salary
        exp.company_2_duration = cmp_2_duration

        exp.company_3_name = cmp_3_name
        exp.company_3_designation = cmp_3_designation
        exp.company_3_salary = cmp_3_salary
        exp.company_3_duration = cmp_3_duration
        try:
            exp.save()
            print("employee experience insert successfully")
            error="no"
        except:
            error="yes"
            print(f"Error are == {error}")
    return render(request, 'edit_exp.html',{'experience':exp})

def emp_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    education = Employee_Education_history.objects.get(user=user)
    print(f"Education == {education}")
    return render(request, 'emp_education.html',{'education':education})

def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    education = Employee_Education_history.objects.get(user=user)
    print(f"Edit Education == {education}")
    if request.method == 'POST':
        course_pg = request.POST['pg_course']
        college_pg = request.POST['pg_college_name']
        passing_year_pg = request.POST['pg_passing_yr']
        percentage_pg = request.POST['pg_percentage']

        course_g = request.POST['g_course']
        college_g = request.POST['g_college_name']
        passing_year_g = request.POST['g_passing_yr']
        percentage_g = request.POST['g_percentage']

        course_ss = request.POST['course_12']
        school_ss = request.POST['school_12']
        passing_year_ss = request.POST['passing_yr_12']
        percentage_ss = request.POST['percentage_12']

        school_hs = request.POST['school_10']
        passing_year_hs = request.POST['passing_yr_10']
        percentage_hs = request.POST['percentage_10']

        # update record in Education table:
        education.course_pg = course_pg
        education.college_pg = college_pg
        education.passing_year_pg = passing_year_pg
        education.percentage_pg = percentage_pg

        education.course_g = course_g
        education.college_g = college_g
        education.passing_year_g = passing_year_g
        education.percentage_g = percentage_g

        education.course_ss = course_ss
        education.school_ss = school_ss
        education.passing_year_ss = passing_year_ss
        education.percentage_ss = percentage_ss

        education.school_hs = school_hs
        education.passing_year_hs = passing_year_hs
        education.percentage_hs = percentage_hs

        try:
            education.save()
            print("Education details successfully updated")
            error = ""
        except:
            error="yes"     
            print(f"Error is : {error}")
    return render(request, 'edit_education.html',{'education':education})

def change_password(request):
    user = request.user
    print(f"current user == {user}")
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password!=confirm_password:
            print("both password didn't match ! Please try again")
        else:
            try:
                if user.check_password(current_password):
                    user.set_password(new_password)
                    print("password is available")
                    user.save()
                    print("password is set successfully")
                else:
                    print("password is not available")    
            except:
                error = "yes"
                print(f"Error occured !! {error}")
    return render(request, 'change_password.html')