from django.urls import path
from .views import (all_vacancies, vacancies_by_direction, vacancy_detail, vacancy_update, vacancy_create,
                    vacancy_delete, all_directions, direction_delete, direction_create, direction_update)
urlpatterns = [
    path('', all_vacancies, name="index"),
    path('direction/<int:direction_id>/', vacancies_by_direction, name="vacancies_by_direction"),
    path('vacancy-create/', vacancy_create, name="vacancy_create"),
    path('vacancy-detail/<int:pk>/', vacancy_detail, name="vacancy_detail"),
    path('vacancy-update/<int:pk>/', vacancy_update, name="vacancy_update"),
    path('vacancy-delete/<int:pk>/', vacancy_delete, name="vacancy_delete"),
    path('all-direction/', all_directions, name="all_directions"),
    path('direction-create/', direction_create, name="direction_create"),
    path('direction-update/<int:pk>', direction_update, name="direction_update"),
    path('direction-delete/<int:pk>', direction_delete, name="direction_delete"),
]
