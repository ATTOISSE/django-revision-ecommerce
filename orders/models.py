from django.db import models as m
from uuid import uuid4

class Client(m.Model):
    first_name = m.CharField(max_length=40)
    last_name = m.CharField(max_length=50)
    age = m.IntegerField()
    email = m.EmailField()
    password = m.CharField()

class Command(m.Model):
    id = m.AutoField(primary_key=True)
    command_number = m.UUIDField(default=uuid4)
    created_at = m.DateTimeField(auto_now_add=True)
    client = m.ForeignKey(Client,on_delete=m.deletion.CASCADE,related_name='commands')

class Product(m.Model):
    wording = m.CharField()
    price = m.IntegerField()
    stock = m.SmallIntegerField(null=True)
    description = m.TextField()
    picture = m.ImageField(upload_to='product/',null=True)
    command = m.ForeignKey(Command,on_delete=m.deletion.CASCADE,related_name='products',null=True)

class Category(m.Model):
    id = m.AutoField(primary_key=True)
    name = m.CharField()
    products = m.ManyToManyField(Product,related_name='categories',null=True)

