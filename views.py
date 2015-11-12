# -*- coding: utf-8 -*-
"test for lab4 R5&R6"
from django.shortcuts import render_to_response
from django.shortcuts import render
#from django.http import HttpResponseRedirect
from django.http import HttpResponse
from models import Book
from models import Author

# Create your views here.
def index(request):
    return render_to_response('index.html')
def searchAuthor(request):
    return render_to_response('searchAuthor.html')
def searchResult(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            try:
                author1 = Author.objects.get(Name=q)
                authorid = author1.AuthorID
                book1 = []
                for book in Book.objects.all():
                    if book.AuthorID == authorid:
                        book1.append(book)
                return render_to_response('searchResult.html',{'author1': author1,'book1': book1})
            except:
                return render_to_response('searchFailure.html')
    return render_to_response('searchAuthor.html',{'error': error})
def BookDetail(request):
    if 'isbn' in request.GET and 'id' in request.GET:
        Isbn = request.GET['isbn']
        ID = request.GET['id']
        book1 = Book.objects.get(ISBN = Isbn)
        author1 = Author.objects.get(AuthorID = ID)
    return render_to_response('BookDetail.html',{'author1': author1,'book1': book1})
def delete(request):
    if 'isbn' in request.GET:
        Isbn = request.GET['isbn']
        book1 = Book.objects.get(ISBN = Isbn)
        Book.delete(book1)
    return render_to_response('delete.html')
def update(request):
    if 'isbn' in request.GET:
        Isbn = request.GET['isbn']
        book1 = Book.objects.get(ISBN = Isbn)
    return render_to_response('update.html',{'book1': book1})
def updateBook(request):
    book1 = Book()
    if request.POST:
        book1.ISBN = request.POST['ISBN']
        book1.Title = request.POST['Title']
        book1.AuthorID = request.POST['AuthorID']
        book1.Publisher = request.POST['Publisher']
        book1.PublishDate = request.POST['PublishDate']
        book1.Price = request.POST['Price']
        if book1.ISBN and book1.Title and book1.AuthorID:
            book1.save()
            authorid = book1.AuthorID
            try:
                author = Author.objects.get(AuthorID = authorid)
                return render(request,'updateBookSucceed.html')
            except:
                return render(request,'NoneAuthor.html')
        else:
            return render(request,'updateBookFailure.html',{'book1': book1})
    return render_to_response('updateBook.html')
def addAuthor(request):
    author1 = Author()
    return render(request,'addAuthor.html',{'Author':author1})
def addAuthorSucceed(request):
    author1 = Author()
    if request.POST:
        author1.AuthorID = request.POST['AuthorID']
        author1.Name = request.POST['Name']
        author1.Country = request.POST['Country']
        author1.Age = request.POST['Age']
        if author1.AuthorID and author1.Name:
            id1 = author1.AuthorID
            try:
                q = Author.objects.get(AuthorID = id1)
                return render(request,'existAuthorID.html',{'author1':q})
            except:
                author1.save()
                return render(request,'addAuthorSucceed.html')
        else:
            return render(request,'addAuthorFailure.html')
def addBook(request):
    book1 = Book()
    return render(request,'addBook.html',{'Book':book1})
def addBookSucceed(request):
    book1 = Book()
    if request.POST:
        book1.ISBN = request.POST['ISBN']
        book1.Title = request.POST['Title']
        book1.AuthorID = request.POST['AuthorID']
        book1.Publisher = request.POST['Publisher']
        book1.PublishDate = request.POST['PublishDate']
        book1.Price = request.POST['Price']
        if book1.ISBN and book1.Title and book1.AuthorID:
            authorid = book1.AuthorID
            bookisbn = book1.ISBN
            try:
                book = Book.objects.get(ISBN = bookisbn)
                return render(request,'existBookISBN.html',{'book1':book})
            except:
                book1.save()
                try:
                    author = Author.objects.get(AuthorID = authorid)
                    return render(request,'addBookSucceed.html')
                except:
                    return render(request,'NoneAuthor.html')
        else:
            return render(request,'addBookFailure.html')
            
