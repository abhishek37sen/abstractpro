from django.contrib import admin
from .models import Customer,Student,Emp

class AdminStudent(admin.ModelAdmin):
    list_display = ['name','location','marks']

class AdminEmp(admin.ModelAdmin):
    list_display = ['name','location','salary']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','location','sales']

admin.site.register(Emp,AdminEmp)
admin.site.register(Student,AdminStudent)
admin.site.register(Customer,AdminCustomer)