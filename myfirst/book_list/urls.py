from django.urls import path

from . import views


app_name = 'book_list'
# python будет доставать вьюшку исключительно из этого приложение приложений может быть много

urlpatterns = [
    path('', views.index, name='index'), # страница
    path('<int:article_id>/', views.detail, name='detail'),# страница книги
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('add_a_book', views.add_a_book, name='add_a_book')
]
