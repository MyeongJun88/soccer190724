from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request, 'shopping/shop.html')
  
    
def item1(request):
    return render(request, 'shopping/item1.html')
  
    
def item2(request):
    return render(request, 'shopping/item2.html')
