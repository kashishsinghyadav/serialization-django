from django.contrib import admin

from .models import Student

class Stu_admin(admin.ModelAdmin):
    list_display=('id','name','roll_no','city')

admin.site.register(Student,Stu_admin)

# Register your models here.
