from django.views.generic import ListView, CreateView, TemplateView
from .models import Product

class HomeView(TemplateView):
    template_name = 'home.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_add.html'