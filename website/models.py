from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('Trainee', 'Trainee'),
    ('Trainer', 'Trainer'),
)

class Person(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    school_name = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
