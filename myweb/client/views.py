from django.shortcuts import render,redirect
from client import forms
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView,CreateView,ListView
from main.models import Product
# Create your views here.

class Home(TemplateView):
    products=Product
    def get(self,request,*args,**kwargs):
        products = Product.objects.all()
        context = {"products": products}
        return render(request, "home.html", context)


    template_name="home.html"
#class SignUpView(TemplateView):
#    def get(self, request, *args, **kwargs):
#        form = forms.UserRegistrationForm()
#        context = {"form": form}
#        return render(request,"userregistration.html",context)
#   def post(self,request):
#        form = forms.UserRegistrationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            print("user hasbeen registered")
#            return redirect("signin")
def sign_up(request):
    form=forms.UserRegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user hasbeen registered")
            return redirect("signin")
        else:
            context["form"]=form
            return render(request, "registration.html", context)

    return render(request,"registration.html",context)


def sign_in(request):
    form=forms.LoginForm()
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")

    return render(request,"login.html",{"form":form})


def sign_out(request):
    logout(request)
    return redirect("signin")