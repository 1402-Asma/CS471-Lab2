from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Book, Student, Address, Department, Course, Student1, Student2, Student3
from django.db.models import Q, Count, Sum, Min, Max, Avg
from .forms import BookForm, StudentForm, StudentForm3

# def index(request):
#     name = request.GET.get("name") or "world!"  #add this line
#     #return render(request, "bookmodule/index.html")   
#     #return render(request, "bookmodule/index.html" , {"name": name})  #your render line 
#     return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name


# def index2(request, val1 = 0):   #add the view function (index2)
#     return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request, id):
    return render(request,'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tabels(request):
    # mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook = Book.objects.create(title = 'Reversing: Secrets of Reverse Engineer', author = 'E. Eilam',price = 97.0, edition = 1)
    mybook = Book.objects.create(title = 'The Hundred-Page Machine Learning', author = 'Andriy Burkov',price = 100.0, edition = 4)
    mybook.save()
    return render(request, "bookmodule/tabels.html")

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def task1(request):
    mybooks=Book.objects.filter(Q(price__lte = 80))
    return render(request, 'bookmodule/task1.html',{'books':mybooks})

def task2(request):
    mybooks=Book.objects.filter(Q(edition__gt = 3) & (Q(title__contains = 'CO')|Q(author__contains = 'CO')))
    return render(request, 'bookmodule/task2.html',{'books':mybooks})

def task3(request):
    mybooks=Book.objects.filter(~Q(edition__gt = 3) & (~Q(title__contains = 'CO')| ~Q(author__contains = 'CO')))
    return render(request, 'bookmodule/task2.html',{'books':mybooks})

def task4(request):
    mybooks=Book.objects.order_by('title')
    return render(request, 'bookmodule/task1.html',{'books':mybooks})

def task5(request):
    agg = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html',{'agg':agg})

def task1_9(request):
    data = Department.objects.annotate(num_students= Count('student1'))
    return render(request, 'bookmodule/task1_9.html',{'departments':data})

def task2_9(request):
    data = Course.objects.annotate(num_students= Count('student1'))
    return render(request, 'bookmodule/task2_9.html', {'courses':data})

def task3_9(request):
    oldest_students = []
    departments = Department.objects.all()

    for dept in departments:
        oldest_student = Student1.objects.filter(department=dept).order_by('id').first()
        if oldest_student:
            oldest_students.append({
                'department': dept.name,
                'student_name': oldest_student.name,
                'student_id': oldest_student.id
            })
    return render(request, 'bookmodule/task3_9.html', {'oldest_students': oldest_students})

def task4_9(request):
    departments = Department.objects.annotate(student_count=Count('student1')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/task4_9.html',{'departments':departments})


def studentsbycity(request):
    data = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/students_by_city.html', {'data': data})

def complex_query(request):
    mybooks=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, "bookmodule/search.html")

def list_books10(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price =request.POST['price']
        )
        return redirect('list_books')
    return render(request, 'bookmodule/addbook.html')

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/editbook.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')


#------------------------Form------------------------
def list_books10_2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks2.html', {'books': books})

def add_book_2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/addbook2.html', {'form': form})

def edit_book_2(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/editbook2.html', {'form': form})

def delete_book_2(id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books_2')

#----------------------Lab11----------------------------
def list_student(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/list_student.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_student')
    else:
        form = StudentForm()
    return render (request, 'bookmodule/addStudent.html', {'form': form})

def update_student(request, id):
    student = Student2.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_student')
    else:
        form = StudentForm(instance=student)
    return render (request, 'bookmodule/updateStudent.html', {'form': form})

def delete_student(request,id):
    student = Student2.objects.get(id=id)
    student.delete()
    return redirect('list_student')
#---------------------------task2-------------------------------
def list_student3(request):
    students = Student3.objects.all()
    return render(request, 'bookmodule/list_student2.html', {'students': students})

def add_student3(request):
    if request.method == 'POST':
        form = StudentForm3(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_student3')
    else:
        form = StudentForm3()
    return render (request, 'bookmodule/addStudent2.html', {'form': form})

def update_student3(request, id):
    student = Student3.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm3(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_student3')
    else:
        form = StudentForm3(instance=student)
    return render (request, 'bookmodule/updateStudent2.html', {'form': form})

def delete_student3(request,id):
    student = Student3.objects.get(id=id)
    student.delete()
    return redirect('list_student3')
   
def view_image(request):
    students = Student3.objects.filter(~Q(photo=''), photo__isnull=False)
    return render(request, 'bookmodule/viewImage.html', {'students': students})
    

