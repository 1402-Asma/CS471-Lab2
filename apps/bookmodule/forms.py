from django import forms
from .models import Book,Student2, Address2, Student3, Address3

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']
        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the city' 
            })
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'student name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'age'
            }),
            'address': forms.Select(attrs={
                'class': 'form-control',
            })
        }
        
class StudentForm3(forms.ModelForm):
    class Meta:
        model = Student3
        fields = ['name', 'age', 'address','photo']
     
    name= forms.CharField(
            widget = forms.TextInput(attrs={
                'placeholder': 'student name'
            })
    )
    age= forms.IntegerField(
            widget = forms.TextInput(attrs={
                'placeholder': 'age'
            })
    )
    address= forms.ModelMultipleChoiceField(
            queryset= Address3.objects.all(),
            widget =forms.CheckboxSelectMultiple()
    )

