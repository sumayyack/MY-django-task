from django.shortcuts import render
from main.forms import ProductForm
from main.models import Product
from django.views.generic import TemplateView,CreateView,ListView
from django.urls import reverse_lazy
# Create your views here.

class CreateProduct(CreateView):

        model = Product
        form_class = ProductForm
        template_name = "add_property.html"
        success_url = reverse_lazy("addproduct")

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["products"] = self.model.objects.all()
            return context

class ProductList(ListView):











    model= Product
    template_name = "product_list.html"
    context_object_name = "products"
