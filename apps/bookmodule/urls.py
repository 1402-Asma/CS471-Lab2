from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links , name='books.links'),
    path('html5/text/formatting/', views.formatting , name='books.formatting'),
    path('html5/listing/', views.listing , name='books.listing'),
    path('html5/tabels/', views.tabels , name='books.tabels'),
    path('search/', views.search , name='books.search'),
    path('simple/query', views.simple_query  , name='books.simple_query'),
    path('complex/query', views.complex_query  , name='books.lookup_query'),
    path('lab8/task1', views.task1  , name='books.task1'),
    path('lab8/task2', views.task2  , name='books.task2'),
    path('lab8/task3', views.task3  , name='books.task3'),
    path('lab8/task4', views.task4  , name='books.task4'),
    path('lab8/task5', views.task5  , name='books.task5'),
    path('students/by-city/', views.studentsbycity, name='students_by_city'),
]
