from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from .models import *
from .forms import *

def home(request):
    return render(request, 'list/home.html')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'list/book_list.html', {'books': books})
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year_published = request.POST.get('year_published')
        rating = request.POST.get('rating')

        book.title = title
        book.author = author
        book.year_published = year_published
        book.rating = rating
        book.save()
        return redirect('book_detail', slug=book.slug)
    return render(request, 'list/book_detail.html', {'book': book})
def book_update(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == "POST":
        return redirect('book_detail', slug=book.slug)
    return render(request, 'list/book_update.html', {'book': book})
def book_delete(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        return redirect('book_list')
    return render(request, 'list/book_delete.html', {'book': book})
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        year_published = request.POST.get('year_published')
        genre_ids = request.POST.getlist('genres')
        rating = request.POST.get('rating')
        author = get_object_or_404(Author, id=author_id)
        genres = Genre.objects.filter(id__in=genre_ids)

        book = Book.objects.create(
            title=title,
            slug=slugify(title),
            author=author,
            year_published=year_published,
            rating=rating
        )
        book.genres.set(genres)
        return redirect('book_list')
    authors = Author.objects.all()
    genres = Genre.objects.all()
    return render(request, 'list/book_create.html', {'authors': authors, 'genres': genres})
def add_author(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        print(f"Received first_name: {first_name}")
        print(f"Received last_name: {last_name}")

        author = Author.objects.create(
            first_name=first_name,
            last_name=last_name
        )
        return redirect('book_create')
    return render(request, 'list/add_author.html')
def add_genre(request):
    form = GenreForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            genre = Genre.objects.create(name=name)
            return redirect('home')
    return render(request, 'list/add_genre.html', {'form': form})