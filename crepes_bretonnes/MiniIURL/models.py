from django.db import models
from django.utils import timezone

import random
import string


class MiniURL(models.Model):
    url = models.URLField(unique=True)
    mini_url = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Date de création")
    created_by = models.CharField(max_length=40, verbose_name="Créé par")
    nb_access = models.SmallIntegerField(default=0, verbose_name="nombre de redirections")

    def __str__(self):
        return "[{0}] {1}".format(self.mini_url, self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate(6)

        super(MiniURL, self).save(*args, **kwargs)

    def generate(self, nb_caractere):
        chars = string.ascii_letters + string.digits
        aleatoire = [random.choice(chars) for _ in range(nb_caractere)]

        self.mini_url = ''.join(aleatoire)

    class Meta:
        verbose_name = "Mini Url"
        verbose_name_plural = "Minis URL"
