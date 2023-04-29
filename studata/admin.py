from django.contrib import admin
from .models import StudentInfo
# Register your models here.
@admin.register(StudentInfo)
class AdminStudentinfo(admin.ModelAdmin):
    list_display = [
        'name',
        'roll',
        'city'
    ]