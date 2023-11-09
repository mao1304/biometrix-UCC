from django.contrib import admin
from .models import  NewUser, faltas
from .forms import NewUserForm, AdminUserForm
from django.contrib.auth.admin import UserAdmin


@admin.register(faltas)
class faltasAdmin(admin.ModelAdmin):
    pass


class NewUserAdmin(UserAdmin):
    add_form = NewUserForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('username', 'password', 'first_name', 'last_name','huella', 'is_staff'),

        }),
    )

admin.site.register(NewUser, NewUserAdmin)

