from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import UserForm, BookForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Book, Book_User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def auth(request):
	if not request.user.is_authenticated():
		error=""
		if request.method == "POST":
			form=UserForm(request.POST)
			if form.is_valid():
				username = request.POST['username']
				password = request.POST['password']
				user = authenticate(username=username, password=password)
				if request.POST.get('reg'):
					var=User(username=username)
					var.save()
					var = User.objects.get(username=username)
					var.set_password(password)
					var.save()
					return redirect('bookshop.views.main')
				elif user is not None:			
					if user.is_active:
						login(request, user)
						return redirect('bookshop.views.main')
				else:
					form=UserForm()
					error="wrong"		
		else:
			form = UserForm()
		return render(request, 'bookshop/auth.html',{'form': form, 'error':error})
	else:
		return redirect('bookshop.views.main')
def main(request):
	if request.user.is_staff:
		admin=True;
	else:
		admin=False
	book_list=Book.objects.all()
	paginator = Paginator(book_list, 4) # Show 4 contacts per page
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		books = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		books = paginator.page(paginator.num_pages)
	return render(request, 'bookshop/main.html',{"books":books,'admin':admin})
def info(request, pk):
	book = get_object_or_404(Book, pk=pk)
	user_list=Book_User.objects.filter(book=pk)

	if request.method == "POST":
		user=request.user.username
		b_u=Book_User(user=user,book=pk)
		b_u.save()
		book.number=book.number-1
		book.save()
	return render(request, 'bookshop/info.html',{'book':book, 'user_list':user_list})

def edit(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			book=form.save(commit=False)
			value=request.FILES.get('img')
			pic=Book(img=value)
			pic=form.save(commit=False)
			pic.save()
			return redirect('bookshop.views.main')
	else:
		form=BookForm(instance=book)
	return render(request, 'bookshop/edit.html',{'form':form})