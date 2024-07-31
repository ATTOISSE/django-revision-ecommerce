from django.shortcuts import render,redirect,get_object_or_404
from .models import Client,Product
from django.contrib.auth.hashers import make_password 
from django.contrib import messages
from .forms.client import Client_form,Product_form

def index(request):
    return render(request,'index.html')


def  client_home(request,*args, **kwargs):
    clients = Client.objects.all()

    return render(request,'client/index.html',{'clients':clients})

def client_create(request, id=None):
    if id:
        client = get_object_or_404(Client, pk=id)
    else:
        client = None
    
    if request.method == 'POST':
        form = Client_form(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.password = make_password(form.cleaned_data['password'])
            client.save()
            if id:
                messages.success(request, 'Le client a été modifié avec succès.')
            else:
                messages.success(request, 'Le client a été ajouté avec succès.')
            return redirect('client.home')  
    else:
        form = Client_form(instance=client)
    
    return render(request, 'client/create.html', {'form': form, 'client': client})

def client_remove(request, id):
    client = get_object_or_404(Client,pk=id)
    if request.method == 'POST':
        client.delete()
        messages.success(request,'le client a été suppimé avec succés !!!',extra_tags='info')
        return redirect('client.home')
    return render(request,'client/index.html',{'client': client})

def product_home(request):
    products = Product.objects.all()
    return render(request,'product/index.html',{'products':products})

def product_catalog(request):
    products = Product.objects.all()
    return render(request,'product/catalog.html',{'products':products})

def product_create(request,id=None):
    if id:
        product = get_object_or_404(Product,pk=id)
    else:
        product = None
    if request.method == 'POST':
        form = Product_form(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            if id:
                messages.success(request,'le produit a été modifié avec succés !!!',extra_tags='warning')
            else:
                messages.success(request,'le produit a été ajouté avec succés !!!')
            return redirect('product.home')
    else:
        form = Product_form(instance=product)
    return render(request,'product/create.html',{'form':form,'product':product})

def product_remove(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request,'le produit à ete supprimé avec succés',extra_tags='info')
        return redirect('product.home')
    return render(request,'product/index.html')
