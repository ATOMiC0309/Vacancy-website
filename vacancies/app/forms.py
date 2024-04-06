from django import forms
from .models import Vacancy, Direction


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'direction', 'company_name', 'work_experience_from', 'work_experience_to'
                  , 'salary_from', 'salary_to', 'about_company', 'required_task', 'convenience', 'skills']


class DirectionFrom(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['title']