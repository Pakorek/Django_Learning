from django.db import models
from django.utils import timezone


class MiniURL(models.Model):
    url = models.URLField(unique=True)
    mini_url = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now(), verbose_name="Date de création")
    created_by = models.CharField(max_length=40, verbose_name="Créé par")
    nb_access = models.SmallIntegerField(verbose_name="nombre de redirections")

    class Meta:
        verbose_name = "Mini Url"
        ordering = ('nb_access', )

    def __str__(self):
        return self.url
