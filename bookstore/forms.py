from .models import Book,UserProfile
from django.contrib.auth.models import User
from django.forms import ModelForm

class NewBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('book_title','book_description','book_image','live_site','book_category')



class ProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','bio', 'contact')
