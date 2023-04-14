from django.shortcuts import render, redirect

from item.models import Category, Item

# Create your views here.


from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    
    return render(request, 'EC_App/index.html',{
        'categories': categories,
        'items' : items,
        
    }
    )


def contact(request):
    return render(request, 'EC_App/contact.html')


def signup(request):
    
    if request.method =='POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
        else:
            form = SignupForm()
    
    return render(request, 'EC_App/signup.html',{
        'form':form
    })

