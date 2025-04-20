from django.contrib import admin
from .models import Book 
from .models import Student
from .models import Student1
from .models import Card, Department, Course

# Register your models here.

admin.register(Book)
admin.register(Student)
admin.register(Card)
admin.register(Student1)
admin.register(Course)
admin.register(Department)

