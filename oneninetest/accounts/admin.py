from django.contrib import admin
from .models import Accounts
# Register your models here.
class AccountsAdmin(admin.ModelAdmin):
    list_display=('username','servername','password')

admin.site.register(Accounts,AccountsAdmin)