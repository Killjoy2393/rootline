from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image
import os


class ContactForm(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Ім'я"))
    email = models.EmailField(verbose_name=_("E-mail"))
    phone = models.CharField(max_length=20, verbose_name=_("Телефон"))
    message = models.TextField(verbose_name=_("Повідомлення"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата відправлення"))

    class Meta:
        verbose_name = _("Форма зворотного зв'язку")
        verbose_name_plural = _("Форма зворотного зв'язку")

    def __str__(self):
        return f"{self.name} - {self.email}"


class HeroSection(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")
    button_text = models.CharField(max_length=100, blank=True, verbose_name="Текст кнопки")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hero секция"
        verbose_name_plural = "Hero секция"

    def __str__(self):
        return f"Hero: {self.title}"

    def save(self, *args, **kwargs):
        """Обрабатывает изображение: сжимает, конвертирует в WebP и сохраняет в базу"""
        super().save(*args, **kwargs)  # Первое сохранение, чтобы получить путь

        img_path = self.image.path

        # Если уже WebP, ничего не делаем
        if img_path.endswith(".webp"):
            return

        # Сжимаем изображение
        self.compress_image(img_path)

        # Конвертируем в WebP
        webp_path = self.convert_to_webp(img_path)

        # Удаляем оригинальный файл
        os.remove(img_path)

        # Обновляем путь к изображению
        self.image.name = os.path.relpath(webp_path, os.path.dirname(img_path))

        # Повторное сохранение модели с новым путём
        super().save(update_fields=['image'])

    def compress_image(self, img_path):
        """Сжимает изображение перед сохранением"""
        try:
            with Image.open(img_path) as img:
                img = img.convert("RGB")
                img.save(img_path, quality=85, optimize=True)
        except Exception as e:
            print(f"Ошибка при сжатии: {e}")

    def convert_to_webp(self, img_path):
        """Конвертирует изображение в WebP"""
        try:
            webp_path = f"{os.path.splitext(img_path)[0]}.webp"
            with Image.open(img_path) as img:
                img.save(webp_path, "WEBP", quality=80)
            return webp_path
        except Exception as e:
            print(f"Ошибка при конвертации в WebP: {e}")
            return img_path  # Если ошибка, возвращаем оригинальный путь

    

class InfoBlock(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Заголовок"))
    caption = models.TextField(verbose_name=_("Опис"))
    span = models.CharField(max_length=100, verbose_name=_("Фіналочка"))
    stats = models.JSONField(verbose_name=_("Stats"), default=list)
    button_text = models.CharField(max_length=100, verbose_name=_("Текст кнопки"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))


    class Meta:
        verbose_name = "Інформаційна секція"
        verbose_name_plural = "Інформаційна секція"

    def __str__(self):
        return self.title
    

class ServicesBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок блоку з послугами"))
    link_text = models.CharField(max_length=255, verbose_name=_("Текст кнопки"), default="Детальніше")


    class Meta:
        verbose_name = "Секція послуг"
        verbose_name_plural = "Секція послуг"


    def __str__(self):
        return self.title
    

class ProjectsBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок блоку з проектами"))
    link_text = models.CharField(max_length=255, verbose_name=_("Текст кнопки"))


    class Meta:
        verbose_name = "Секція проектів"
        verbose_name_plural = "Секція проектів"


    def __str__(self):
        return self.title
    

class ReviewsBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок блоку з відгуками"))
    caption = models.TextField(max_length=255, verbose_name=_("Опис"))


    class Meta:
        verbose_name = "Секція відгуків"
        verbose_name_plural = "Секція відгуків"


    def __str__(self):
        return self.title
    

class ArticlesBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок блоку з відгуками"))
    link_text = models.CharField(max_length=255, verbose_name=_("Текст кнопки"))


    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"


    def __str__(self):
        return self.title
    
    from django.db import models

class MetaData(models.Model):
    meta_description = models.TextField( blank=True, verbose_name="Мета-опис головної сторінки")
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name="Ключові слова")

    class Meta:
        verbose_name = "Метаопис головної сторінки" 
        verbose_name_plural = "Метаопис головної сторінки"

    def __str__(self):
        return self.meta_description[:50]
