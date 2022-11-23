from django.contrib.auth.models import User
from django.db import models

class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    litr = models.PositiveIntegerField()
    batafsil = models.CharField(max_length=300)
    def __str__(self):return self.brend


class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.PositiveIntegerField()
    qarz = models.PositiveIntegerField()
    manzil = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): return self.ism


class Admin(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveIntegerField()
    ish_vaqti = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): return self.ism


class Haydovchi(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.PositiveIntegerField()
    kiritilgan_sana = models.DateTimeField()
    def __str__(self): return self.ism

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    when = models.DateTimeField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    def __str__(self):return f"{self.suv}"

