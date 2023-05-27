import datetime
from django.db import models
from django.utils import timezone

class Book(models.Model):
    book_title = models.CharField('название Книги', max_length=100)
    book_text = models.TextField('Описание книгии')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.book_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        # меняем название класса что бы в админке отображался на русском

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        # меняем название класса что бы в админке отображался на русском



# CharField это тип даных текст обязательный оргумент max_length= для небольшого текста типа заголовки
# TextField это тип даных текс для больших данных статьи
# DateTimeField дата публикации
# ForeignKey модель к каторой должна привязыватся к другой модели
# on_delete=models.CASCADE при удалиние статьи удалятся и все коментарии к ней


