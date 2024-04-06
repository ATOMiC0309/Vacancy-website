from django.db import models

# Create your models here.


class Direction(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Vacancy(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=160)
    work_experience_from = models.IntegerField()
    work_experience_to = models.IntegerField()
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    about_company = models.TextField()
    required_task = models.TextField()
    convenience = models.TextField()
    skills = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']

