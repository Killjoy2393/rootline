from django.db import models
from django.utils.translation import gettext_lazy as _
import os
from PIL import Image
from django.conf import settings

class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Ім'я"))
    position = models.CharField(max_length=255, verbose_name=_("Посада"))
    text = models.TextField(verbose_name=_("Текст відгуку"))
    photo = models.ImageField(upload_to='reviews/', verbose_name=_("Фото"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата створення"))

    class Meta:
        verbose_name = _("Відгук")
        verbose_name_plural = _("Відгуки")
        ordering = ["-created_at"]  # Последние отзывы будут отображаться первыми

    def __str__(self):
        return f"{self.name} – {self.position}"
    
    def save(self, *args, **kwargs):

        """Сжимает изображение, создаёт WebP-версию и заменяет оригинал WebP-файлом"""
        super().save(*args, **kwargs)  # Сохраняем оригинальное изображение

        # Путь к загруженному изображению
        img_path = self.photo.path

        # Сжимаем оригинал (JPEG/PNG)
        self.compress_image(img_path)

        # Конвертируем в WebP
        webp_path = self.convert_to_webp(img_path)

        # Удаляем оригинальное изображение (если оно не WebP)
        if not img_path.endswith(".webp"):
            os.remove(img_path)

        # Обновляем путь в базе данных на WebP-версию
        self.photo.name = os.path.relpath(webp_path, settings.MEDIA_ROOT)
        super().save(update_fields=['photo'])

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
