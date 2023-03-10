from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products, Category
from products.forms import ProductForm

# Create your views here.
def create_product(request):
    if request.method == 'GET': #pasar los campos
        context = {
            'form': ProductForm()
        }
        return render(request, 'products/create_product.html', context=context)
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid(): #creamos el producto
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, 'products/create_product.html', context=context)
        else: #mostramos el formulario
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
        return render(request, 'products/create_product.html', context=context) 


def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Products.objects.filter(name__contains=search)
    else:
        products = Products.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'products/list_products.html', context=context)

def create_category(request, name):
    Category.objects.create(name=name)
    return HttpResponse('Categoria creada')

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'categories/list_categories.html', context=context)