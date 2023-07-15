from django.db import models
from .choise_options import Status, Priority


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.WAITING,
    )
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.HIGH,
    )

    class Meta:  # используем вспомогательный класс мета для сортировки наших дел
        ordering = ["-time_create"]  # сортировка дел по времени их создания

    def __str__(self):
        return self.title