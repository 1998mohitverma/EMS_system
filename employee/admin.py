from django.contrib import admin
from .models import Employee_Details, Employee_Education_history, Employee_Experience
# Register your models here.

admin.site.register(Employee_Details)
admin.site.register(Employee_Education_history)
admin.site.register(Employee_Experience)
