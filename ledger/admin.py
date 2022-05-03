from django.contrib import admin

from .models import Type, Account, Transaction

admin.site.register(Type)
admin.site.register(Account)
admin.site.register(Transaction)