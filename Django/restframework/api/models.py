from django.db import models


class RestRight(models.Model):
    data = models.TextField(max_length=2000)

    class Meta:
        verbose_name_plural = "RestRight"

    def __str__(self):
        return self.data


class RestLeft(models.Model):
    data = models.TextField(max_length=2000)

    class Meta:
        verbose_name_plural = "RestLeft"

    def __str__(self):
        return self.data
