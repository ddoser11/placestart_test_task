from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    COMPLETE = 'Выполнено', _('Выполнено')
    IN_PROCESS = 'В процессе', _('В процессе')
    WAITING = 'Ожидает выполнения', _('Ожидает выполнения')


class Priority(models.TextChoices):
    HIGH = 'Высокий', _('Высокий')
    MIDDLE = 'Средний', _('Средний')
    LOW = 'Низкий', _('Низкий')

