from django.db import models
from safedelete.models import SafeDeleteModel


class Type(SafeDeleteModel):

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True)

    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name

class Account(SafeDeleteModel):

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True)

    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name

class Transaction(SafeDeleteModel):

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True)

    date = models.DateTimeField()

    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.DO_NOTHING)

    type = models.ForeignKey(Type, related_name='transactions', on_delete=models.DO_NOTHING)

    value = models.FloatField(default=0)

    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.date} Account: {self.account}, Value: {self.value}, Type: {self.type}, Description: {self.description}"