from django.db import models
from gpa_calculator.models import Course
from gpa_calculator.calculator import calculate
# Create your models here.

class Archive(models.Model):
    STANDARD = {
        (4.5, '4.5'),
        (4.3, '4.3'),
        (3.7, '3.7')
    }
    SEMESTER={
        ('2020_1','2020 SPRING'),
        ('2020_2','2020 SUMMER'),
        ('2020_3','2020 FALL'),
        ('2020_4','2020 WINTER')
    }
    desiredStandard= models.FloatField(choices=STANDARD, null=True)
    semester=models.CharField(max_length=200,choices=SEMESTER,null=True)
    total_avg=models.FloatField(default=0)
    major_avg=models.FloatField(default=0)
    minor_avg=models.FloatField(default=0)
