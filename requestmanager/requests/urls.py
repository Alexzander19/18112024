# 5. Настройте маршруты
# В файле requests/urls.py настройте маршруты:

# '' — для отображения формы и обработки заявок.
# 'list/' — для отображения списка всех заявок.
# Добавьте маршруты приложения в проект (requestmanager/urls.py):


from django.urls import path

from . import views

urlpatterns = [
    path("", views.create, name="create"),

    path("list/", views.list, name="list")
 
]