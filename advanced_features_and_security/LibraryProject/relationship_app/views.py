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





from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Role-check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')





from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm


@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book')
def edit_book(request):
    return render(request, 'relationship_app/edit_book.html')


@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html')
