from django.shortcuts import render, redirect, get_object_or_404
from.models import Players, Player2 
# Create your views hereself.

def list(request):
    players = Players.objects.all()
    return render(request, 'players/list.html', {'players' : players})
    players2 = Player2.objects.all()
    return render(request, 'players/list.html', {'players2' : players2})

    
def create0(request):
    if request.method == "POST":
        title = request.POST.get('title')
        age = request.POST.get('age')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        image = request.FILES.get('image')
        player = Players(title=title, age=age, description=description, created_at=created_at, image=image)
        player.save()
        return redirect('list')
        
    return render(request, 'players/create0.html')
    
    
def create1(request):
    if request.method == "POST":
        title1 = request.POST.get('title1')
        age1 = request.POST.get('age1')
        description1 = request.POST.get('description1')
        player2 = Player2(title1=title1, age1=age1, description1=description1)
        player2.save()
        return redirect('list')
        
    return render(request, 'players/create1.html')
    
    
def create2(request):
    if request.method == "POST":
        title = request.POST.get('title')
        age = int(request.POST.get('age'))
        description = request.POST.get('description')
        image = request.FILES.get('image')
        player = Players(title=title, age=age, description=description, image=image)
        player.save()
        return redirect('list')
        
    return render(request, 'players/create2.html')
    
    
def create3(request):
    if request.method == "POST":
        title = request.POST.get('title')
        age = int(request.POST.get('age'))
        description = request.POST.get('description')
        image = request.FILES.get('image')
        player = Players(title=title, age=age, description=description, image=image)
        player.save()
        return redirect('list')
        
    return render(request, 'players/create3.html')
    

def show(request, id):
    player = get_object_or_404(Players, pk=id)
    default_view_count = player.view_count
    player.view_count = default_view_count + 1
    player.save()
    return render(request, 'players/show.html', {'player' : player})
    
    
def show2(request, id):
    player2 = get_object_or_404(Player2, pk=id)
    default_view_count = player2.view_count
    player2.view_count = default_view_count + 1
    player2.save()
    return render(request, 'players/show2.html', {'player2' : player2})
    
    
def edit(request, id):
    player =  get_object_or_404(Players, pk=id)
    return render(request, 'players/edit.html', {'player' : player})
    
    
def update(request, id):
    if request.method == "POST":
        player = Players.objects.get(pk=id)
        title = request.POST.get('title')
        age = request.POST.get('age')
        description = request.POST.get('description')
        player.title = title
        player.age = age
        player.description = description
        player.save()
        return redirect('players:show', player.pk )
        
        
def delete(request, id):
    if request.method == "POST":
        player = Players.objects.get(pk=id)
        player.delete()
        return redirect('list')