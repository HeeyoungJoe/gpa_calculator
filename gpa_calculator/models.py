from django.db import models


class Course(models.Model):
    #choices
    TYPE={
        ("MJ","major"),
        ("MN","minor"),
        ("GN","general"),
    }
    STANDARD={
        ("default",4.5),
        ("alt_1",4.3),
        ("alt_2",3.7)
    }
    #fields
    course_name=models.CharField(max_length=200)
    course_type=models.CharField(max_length=200,choices=TYPE)
    grade=models.FloatField()
    credits=models.FloatField()
    standard=models.FloatField(choices=STANDARD,null=True)
    desired_standard=models.FloatField(choices=STANDARD,null=True)