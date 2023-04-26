from django.db import models

from apps.users.models import User  

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_tasks",
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название таска"
    )
    description = models.TextField(
        verbose_name="Описание таска"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to="task_images/",
        verbose_name="Фотография таска"
    )

    def __str__(self):
        return f"User: {self.user}, Title: {self.title}"
    
    class Meta:
        verbose_name= "Таск"
        verbose_name_plural= "Таски"