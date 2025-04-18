from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Book, Student, Address
from django.db.models import Q, Count, Sum, Min, Max, Avg


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

def studentsbycity(request):
    data = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/students_by_city.html', {'data': data})



def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
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



    

