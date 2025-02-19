# Generated by Django 5.1.6 on 2025-02-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Ім'я")),
                ('name_uk', models.CharField(max_length=255, null=True, verbose_name="Ім'я")),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name="Ім'я")),
                ('position', models.CharField(max_length=255, verbose_name='Посада')),
                ('position_uk', models.CharField(max_length=255, null=True, verbose_name='Посада')),
                ('position_en', models.CharField(max_length=255, null=True, verbose_name='Посада')),
                ('text', models.TextField(verbose_name='Текст відгуку')),
                ('text_uk', models.TextField(null=True, verbose_name='Текст відгуку')),
                ('text_en', models.TextField(null=True, verbose_name='Текст відгуку')),
                ('photo', models.ImageField(upload_to='reviews/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
                'ordering': ['-created_at'],
            },
        ),
    ]
