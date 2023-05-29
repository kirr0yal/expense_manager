from django.contrib.auth.models import User
from django.db import models


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    description = models.CharField(max_length=10_000, blank=True, null=True)
    amount = models.IntegerField(default=0)
    evidence = models.FileField(upload_to='evidence/%Y-%m-%d', blank=True, null=True)

    def __str__(self):
        return f"{self.description}: {self.amount}KZT"

    def amount_abs(self) -> int:
        return abs(self.amount)

    def filename(self) -> str:
        return self.evidence.name.split("/")[-1]

