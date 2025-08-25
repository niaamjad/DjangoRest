from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=100)
    FamilyName = models.CharField(max_length=100)
    Code = models.IntegerField()


    def __str__(self):
        return self.Name + " " + self.FamilyName + " - " + str(self.Code)
    

class Scores(models.Model):
    student = models.ForeignKey(Student, on_delete =models.PROTECT)
    score = models.PositiveIntegerField()

    
