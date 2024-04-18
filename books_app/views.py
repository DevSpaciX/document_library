from datetime import datetime, date, timedelta


from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from books_app.forms import CustomUserCreationForm
from books_app.models import Book, User


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
        return Book.objects.all()


class UserDetailView(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'


def borrow_book(request):
    user_id = request.POST.get('user_id')
    book_id = request.POST.get('book_id')

    try:
        user = User.objects.get(id=user_id)
        book = Book.objects.get(id=book_id)
        book.is_borrowed = True
        book.borrowed_due_date = datetime.now() + timedelta(days=30)
        book.save()

        user.borrowed_books.add(book)

        return JsonResponse({'success': True})
    except (User.DoesNotExist, Book.DoesNotExist):
        return JsonResponse({'success': False, 'error': 'User or book not found'})


class BorrowedBooksListView(ListView):
    model = Book
    template_name = 'borrowed_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        print (query)
        if query:
            return Book.objects.filter(
                Q(is_borrowed=True) & Q(borrowers__username__contains=query) |
                Q(author__name__icontains=query) | Q(title__icontains=query)
            )
        return Book.objects.filter(is_borrowed=True)

    def get_context_data(self, **kwargs):
        context = super(BorrowedBooksListView, self).get_context_data(**kwargs)
        context['today'] = date.today()
        context['next_week'] = date.today() + timedelta(days=7)
        return context


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('books')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('books')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('books')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

