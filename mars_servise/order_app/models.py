from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime


class Device(models.Model):
    """Options"""

    class Meta:
        db_table = "devices"
        verbose_name = "Доступна Модифікація"
        verbose_name_plural = "Доступна Модифікація"

        manufacturer = models.TextField(verbose_name="Виробник")
        model = models.TextField(verbose_name="Модель")

        def __str__(self):
            return f"{self.manufacturer} {self>model}"
        

class Customer(models.Model):
    """Кінцеві користувачі модицікацій"""

    class Meta:
        db_table = "customers"
        verbose_name = "Опис контрагента"
        verbose_name_plural = "Опис контрагентів"

    customer_name = models.TextField(verbose_name="Найменовання організації")
    customer_address = models.TextField(verbose_name="Адрес")
    customer_city = models.TextField(verbose_name="Місто")

    def __str__(self):
        return self.castomer_name
    

class DeviceInField(models.Model):
    """Модифікації в полях"""

