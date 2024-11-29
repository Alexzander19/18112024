from django.db import models

# Create your models here.
# 3. Создайте модель заявки
# В файле requests/models.py создайте модель Request с полями:

# name — имя пользователя (строка до 100 символов).
# email — email пользователя.
# message — сообщение от пользователя (текстовое поле).
# submitted_at — дата и время подачи заявки.


class Request(models.Model):
    # name = models.CharField(max_length=100)
    email = models.EmailField(default="example@example.com", max_length=300)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name




