from django.contrib import admin
from .models import  User

# Register your models here.

class UserInline(admin.TabularInline):
    model = User
    extra = 2
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('test',{'fields':['user_id']}),
        ('What',{'fields':['password']}),
    ]
    #inlines = [UserInline]
    list_display = ('user_id','password','e_mail','grade','registration_time')

admin.site.register(User)
