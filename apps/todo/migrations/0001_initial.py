# Generated by Django 4.1.7 on 2023-03-02 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название таска')),
                ('description', models.TextField(verbose_name='Описание таска')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='task_images/', verbose_name='Фотография таска')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Таск',
                'verbose_name_plural': 'Таски',
            },
        ),
    ]