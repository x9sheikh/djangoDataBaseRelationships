from django.db import models

# Create your models here.
class Principle(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    age = models.IntegerField(max_length=64)
    qualification = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.firstName}{self.lastName}"


class College(models.Model):
    collegeName = models.CharField(max_length=64)
    principle = models.OneToOneField(Principle, on_delete='CASCADE')

    def __str__(self):
        return self.collegeName
