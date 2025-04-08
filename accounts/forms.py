from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser

class CustumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username' , 'first_name' , 'last_name' , 'email' , 'age')
        help_texts = {
                'age': 'Iltimos, yoshingizni to‘liq kiriting.',
                }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username' , 'first_name' , 'last_name' , 'email' , 'age')