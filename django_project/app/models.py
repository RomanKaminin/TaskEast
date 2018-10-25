from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
import mptt
from phonenumber_field.modelfields import PhoneNumberField


class Department(MPTTModel):
    class Meta():
        db_table = 'department'
        verbose_name_plural = "Отделы"
        verbose_name = "Отдел"
        ordering = ('tree_id', 'level')
    name = models.CharField(max_length=150, verbose_name="Название Отдела")
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children',
                            verbose_name='Главный отдел',
                            on_delete=models.CASCADE
                            )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
mptt.register(Department, order_insertion_by = ['name'])


class Client(models.Model):
    class Meta():
        verbose_name_plural = "Сотрудники"
        verbose_name = "Сотрудник"

    username = models.CharField(max_length=150, blank=True, verbose_name="Имя")
    first_name = models.CharField( max_length=30, blank=True, verbose_name="Фамилия")
    last_name = models.CharField( max_length=30, blank=True, verbose_name="Отчество")
    born_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    email = models.EmailField(blank=True, verbose_name="E-mail")
    phone_number = PhoneNumberField(blank=True, verbose_name="Телефон")
    start_work_date = models.DateField(blank=True, verbose_name="Дата начала работы")
    end_work_date = models.DateField(blank=True, null=True, verbose_name="Дата окончания работы")
    position = models.CharField(max_length=200, verbose_name="Должность")
    department = TreeForeignKey(Department,
                                blank=True,
                                null=True,
                                related_name='cat' ,
                                verbose_name="Отдел",
                                on_delete=models.CASCADE
                                )


    def __str__(self):
        return self.username

