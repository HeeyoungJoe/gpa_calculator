from django.db import models


class Course(models.Model):
    #choices (what is saved, human readable name)pytho
    TYPE={
        ("MJ","major"),
        ("MN","minor"),
        ("GN","general"),
    }
    STANDARD={
        (4.5,'4.5'),
        (4.3,'4.3'),
        (3.7,'3.7')
    }
    #fields
    course_name=models.CharField(max_length=200)
    course_type=models.CharField(max_length=200,choices=TYPE)
    grade=models.FloatField()
    credits=models.FloatField()
    standard=models.FloatField(choices=STANDARD,null=True)
    desired_standard=models.FloatField(choices=STANDARD,null=True)