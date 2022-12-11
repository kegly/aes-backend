from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Student, Company, HR


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name = 'Студент'
    verbose_name_plural = 'Студенты'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,)


# Re-register UserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(HR)
