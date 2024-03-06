from django.db import models
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Employee(MPTTModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')
    hire_date = models.DateField()
    email = models.EmailField()
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subordinates'
    )
    objects = TreeManager()

    class MPTTMeta:
        order_insertion_by = ['last_name', 'first_name', 'middle_name']
        level_attr = 'mptt_level'
        parent_attr = 'parent'

        def __init__(self):
            self.max_level = 7

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name_plural = 'Employees'
