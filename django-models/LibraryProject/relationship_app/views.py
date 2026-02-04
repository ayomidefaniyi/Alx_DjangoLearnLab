from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book


# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatically log in the user
            return redirect('home')  # redirect to a homepage or library page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

