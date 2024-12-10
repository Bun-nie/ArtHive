from django.shortcuts import render, redirect
from .models import Category, Artwork
from django.contrib.auth.decorators import login_required

# Create your views here.
# Prgrmr: Alimurung

def gallery(request):
    user = request.user
    category = request.GET.get('category')

    if category == None:
        artworks = Artwork.objects.all()
    else:
        artworks = Artwork.objects.filter(category__name = category, category__user = user)

    categories = Category.objects.all()
    # context = {'categories': categories, 'artworks': artworks}
    return render(request, 'homepage/gallery.html', {'categories': categories, 'artworks': artworks, 'user' : user})

@login_required(login_url='login')
def viewArtwork(request, pk):
    artwork = Artwork.objects.get(id=pk)
    return render(request, 'homepage/artwork.html', {'artwork': artwork})

@login_required(login_url='login')
def addArtwork(request):
    user = request.user
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        user = request.user
        artworks = request.FILES.getlist('images', False)

        # if data['category'] != 'none':
        #     category = Category.objects.get(id=data['category'])
        # elif data['category_new'] != ' ':
        #     category, created = Category.objects.get_or_create(
        #         user = user, 
        #         name = data['category_new'])
        # else:
        #     pass

        category_new = data.get('category_new', '')
        if data.get('category') != 'none':
            category = Category.objects.get(id=data['category'])
        elif category_new.strip():
            category, created = Category.objects.get_or_create(
                user=user,
                name=category_new
            )
        else:
            category = None

        artName = data.get('artName', '')

        # aw stands for artwork. i can't make another variable using 'artwork' as it is being used inside the for loop  
        for aw in artworks:
            artwork = Artwork.objects.create(
                user = user,
                category = category,
                artName = artName,
                description = data['description'],
                artwork = aw,
            )
        return redirect('base:gallery')

    context = {'categories': categories}
    return render(request, 'homepage/add.html', context)

@login_required
def addComment(request):
    context = {'comments': comments}
    return render(request, 'homepage/artwork.html', context)