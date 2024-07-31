from django import forms
from ..models import Client
from ..models import Product

class Client_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name','last_name','age','email','password']
        labels = {
            'first_name' : 'Nom',
            'last_name' : 'Prenom',
            'age' : 'Age',
            'email' : 'Email',
            'password' : 'Mot de passe',
        }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'age' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
        }

class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['wording','price','stock','description','picture']
        labels = {
            'wording':'Libelle',
            'price':'Prix',
            'stock':'Stock',
            'description':'Description',
            'picture':'Image'
        }

        widgets = {
            'wording': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'stock': forms.TextInput(attrs={'class':'form-control'}),
            'discription': forms.Textarea(attrs={'class':'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class':'form-control'})
        }
