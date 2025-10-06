from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, default="Sonstiges")  # neu

    def __str__(self):
        return f"{self.name} ({self.quantity})"


    class Meta:
        unique_together = ('owner', 'name')  # Ein User kann keinen doppelten Item-Namen haben

    def __str__(self):
        return f"{self.name} ({self.quantity})"
