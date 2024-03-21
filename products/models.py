from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=64)

    def __repr__(self) -> str:
        return f"{self.pk}: {self.name}"
    
    __str__ = __repr__

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(null=True, blank=True)
    family = models.ForeignKey(Family, related_name="users", on_delete=models.CASCADE)  # CASCADE: Userが削除されたら子Entryも削除

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    is_checked = models.BooleanField(default=False)
    price = models.IntegerField(default=0, null=True, blank=True)
    family = models.ForeignKey(Family, related_name="products", on_delete=models.CASCADE)  # CASCADE: Userが削除されたら子Entryも削除
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)