from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Book, Comment # импорт модели из models.py

def index(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5] #показываеть последнии 5книг
    return render(request,"book_list/list.html", {'latest_book_list':latest_book_list}) # все это лежит в папке templates

def detail(request, article_id):
    try:
        a = Book.objects.get(id=article_id)
    except:
        raise Http404("Книга не найдена!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request,'book_list/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Book.objects.get(id=article_id)
    except:
        raise Http404("Нечего нет.")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('book_list:detail', args=(a.id,)))

def add_a_book(request):
    tasks = Book.objects.all()
    return render(request, 'book_list/add_book.html', {'title':'Страница сайта', 'tasks':tasks})

