"""books_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from books_app.views import BookListView, borrow_book, BorrowedBooksListView, login_view, logout_view, register_view, UserDetailView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', view=BookListView.as_view(), name='books'),
    url(r'^borrow_book', view=borrow_book, name='borrow_book'),
    url(r'^borrowed_books/', view=BorrowedBooksListView.as_view(), name='borrowed_books'),
    url(r'^user/(?P<pk>\d+)/', view=UserDetailView.as_view(), name='user_profile'),
    url(r'^login/', view=login_view, name='login'),
    url(r'^logout/', view=logout_view, name='logout'),
    url(r'^register/', view=register_view, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
