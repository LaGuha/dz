from django import forms
from .models import Book

class UserForm(forms.Form):
	username=forms.CharField(label="Логин", max_length=30, required=True)
	password=forms.CharField(label="Пароль", required=True)

class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=['name','author','cover','number','img','desc']
		labels={
			"name": "Название",
			'author':"Автор",
			'cover':"Переплет",
			'number':"Количество",
			'img':"Обложка",
			'desc':"Описание"
		}

		