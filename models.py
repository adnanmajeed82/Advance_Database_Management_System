from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=20)
    plo = models.CharField(max_length=100)
    peo = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):   # Capitalized (best practice)
    std_name = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.std_name