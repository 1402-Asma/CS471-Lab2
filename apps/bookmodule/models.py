from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

class Address(models.Model):
    city = models.CharField(max_length=100)
    
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
class Card(models.Model):
    card_number = models.IntegerField()

class Department(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=50)
    code =  models.IntegerField()
    
class Student1(models.Model):
    name = models.CharField(max_length=100)
    crad = models.OneToOneField(Card,  on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)


class Address2(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.OneToOneField(Address2, on_delete=models.CASCADE)
    
class Address3(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city

class Student3(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ManyToManyField(Address3)
    photo = models.ImageField(upload_to='student/', null=True, blank=True)