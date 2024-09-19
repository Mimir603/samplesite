from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import DateTimeRangeField, ArrayField, HStoreField, CICharField
from django.db import models


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=30)
    notes = GenericRelation('Note')

    def __str__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare, through='Kit',
                                   through_fields=('machine', 'spare'))
    notes = GenericRelation('Note')

    def __str__(self):
        return self.name


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.machine} ({self.spare}): {self.count} шт.'


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field='content_type',
        fk_field='object_id',
    )


# class Message(models.Model):
#     content = models.TextField()
#
#
# class PrivateMessage(Message):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.OneToOneField(Message, on_delete=models.CASCADE, parent_link=True)


# class Message(models.Model):
#     content = models.TextField()
#     name = models.CharField(max_length=20)
#     email = models.EmailField()
#
#     class Meta:
#         abstract=True
#         ordering = ['name']
#
#
# class PrivateMessage(Message):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#     email = None
#
#     class Meta(Message.Meta):
#         pass


class PGSRoomReserving(models.Model):
    name = models.CharField(max_length=20, verbose_name='номер')
    reserving = DateTimeRangeField(verbose_name='Дата резервирования')
    canceled = models.BooleanField(default=False, verbose_name='Отменить резервирование')


class PGSRubric(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    description = models.TextField(verbose_name='Описание')
    tags = ArrayField(base_field=models.CharField(max_length=20), verbose_name='Теги')


class PGSProject2(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    platforms = HStoreField(verbose_name="Использованые платформы")


class PGSProject2(models.Model):
    name = CICharField(max_length=40, verbose_name='Название')
    data = models.JSONField()

