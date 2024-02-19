from django.shortcuts import render, HttpResponse

from .models import*
# Create your views here.
def home(request):
   
   info= Home.objects.all()
   
   data={
      'info':info
   }
   return render(request,'home.html',data)

def about(request):
   story = About.objects.all()
   te = company_info.objects.all()
   
   data={
      's':story,
      't': te
   }
   
   return render(request,'about.html',data)

def contact(request):
   return render(request,'contact.html')

def menu(request):
   items = Menu.objects.all()
   data={
      'item':items
   } 
   
   return render(request,'menu.html',data)
