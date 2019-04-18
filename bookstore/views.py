from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max,F
from .models import UserProfile,Book
from .forms import NewBookForm,ProfileEditForm
from django.urls import reverse
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,'index.html',{'books':books})


@login_required(login_url='/accounts/login/')
def profile(request):
    profile = UserProfile.objects.filter(user = request.user).first()
    

    if request.method == 'POST':
        form = ProfileEditForm(request.POST,instance=profile,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'profile':profile,
        'form':form,
    }
    return render(request,'profile.html',context)



@login_required(login_url='/accounts/login/')
def submit_book(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBookForm(request.POST,request.FILES)

        if form.is_valid():
            book = Book(book_title=request.POST['book_title'],book_image=request.FILES['book_image'],book_description=request.POST['book_description'],book_category= request.POST['book_category'],live_site=request.POST['live_site'],user=request.user)
            book.save()
            return redirect(reverse('index'))
    else:
        form = NewBookForm()

    return render(request,'submit_book.html',{'form':form})


def search_book(request):
    try:
        if 'book' in request.GET and request.GET['book']:
            searched_term = (request.GET.get('book')).title()
            searched_book = Book.objects.get(book_category__icontains = searched_term.title())
            return render(request,'search.html',{'book':searched_book})
    except (ValueError,Book.DoesNotExist):
        raise Http404()

    return render(request,'search.html')

def search_category(request):
    
    if 'category' in request.GET and request.GET['category']:
        search_term = (request.GET.get('category')).title()
        searched_images = Book.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{'message':message,'book_images':searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request,'search.html',{'message':message})


def book(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'book.html',{'book':book})

