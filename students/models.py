from django.db import models

class Student(models.Model):
    STATUS_CHOICES = (
        ('Applied', 'Applied'),
        ('Interviewing', 'Interviewing'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course_interest = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')

    def __str__(self):
        return self.name
