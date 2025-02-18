from django.db import models
from django.utils.translation import gettext_lazy as _

class About(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    text = models.TextField(verbose_name=_("Text"))
    meta_description = models.TextField(blank=True, verbose_name="Мета-опис сторінки про нас")
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name="Ключові слова")

    class Meta:
        verbose_name = _("Про нас")
        verbose_name_plural = _("Про нас")

    def __str__(self):
        return self.title
