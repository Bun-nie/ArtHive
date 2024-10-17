from django.shortcuts import render, redirect
from .models import Category, Artwork
from django.contrib.auth.decorators import login_required

# Create your views here.
# Prgrmr: Alimurung

@login_required(login_url='base: login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')

    if category == None:
        artworks = Artwork.objects.filter(category__user = user)
    else:
        artworks = Artwork.objects.filter(category__name = category, category__user = user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'artworks': artworks}
    return render(request, 'homepage/gallery.html', context)

@login_required(login_url='base: login')
def viewArtwork(request, pk):
    artwork = Artwork.objects.get(id=pk)
    return render(request, 'homepage/artwork.html', {'artwork': artwork})

@login_required(login_url='base: login')
def addArtwork(request):
    user = request.user
    categories = user.category_set.all()
    
    if request.method == 'POST':
        data = request.POST
        artworks = request.FILES.getlist('images', False)

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != ' ':
            category, created = Category.objects.get_or_create(
                user = user, 
                name = data['category_new'])
        else:
            category = None

        # aw stands for artwork. i can't make another variable using 'artwork' as it is being used inside the for loop  
        for aw in artworks:
            artwork = Artwork.objects.create(
                category = category,
                description = data['description',],
                aw = aw,
            )
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'homepage/add.html', context)
