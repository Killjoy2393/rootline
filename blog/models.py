from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import os
from PIL import Image
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    text = models.TextField(verbose_name=_("Text"))
    image = models.ImageField(upload_to='blog/', verbose_name=_("Image"))
    meta_description = models.TextField(blank=True, verbose_name="Мета-опис сторінки статті")
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name="Ключові слова")
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    published_at = models.DateTimeField(default=timezone.now, verbose_name=_("Published At"))

    class Meta:
        verbose_name = _("Стаття")
        verbose_name_plural = _("Статті")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        """Сжимает изображение, создаёт WebP-версию и заменяет оригинал WebP-файлом"""
        super().save(*args, **kwargs)  # Сохраняем оригинальное изображение

        # Путь к загруженному изображению
        img_path = self.image.path

        # Сжимаем оригинал (JPEG/PNG)
        self.compress_image(img_path)

        # Конвертируем в WebP
        webp_path = self.convert_to_webp(img_path)

        # Удаляем оригинальное изображение (если оно не WebP)
        if not img_path.endswith(".webp"):
            os.remove(img_path)

        # Обновляем путь в базе данных на WebP-версию
        self.image.name = os.path.relpath(webp_path, settings.MEDIA_ROOT)
        super().save(update_fields=['image'])

    def compress_image(self, img_path):
        """Сжимает оригинальное изображение перед сохранением"""
        img = Image.open(img_path)
        img = img.convert("RGB")  # Преобразуем в RGB (чтобы избежать проблем с PNG)
        img.save(img_path, quality=85, optimize=True)

    def convert_to_webp(self, img_path):
        """Создаёт WebP-версию изображения"""
        img = Image.open(img_path)
        webp_path = f"{os.path.splitext(img_path)[0]}.webp"
        img.save(webp_path, "WEBP", quality=80)
        return webp_path

    def __str__(self):
        return self.title


class MetaData(models.Model):
    meta_description = models.TextField(blank=True, verbose_name="Мета-опис сторінки блогу")
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name="Ключові слова сторінки блогу")

    class Meta:
        verbose_name = "Метаопис сторінки блогу" 
        verbose_name_plural = "Метаопис сторінки блогу"

    def __str__(self):
        return self.meta_description[:50] 