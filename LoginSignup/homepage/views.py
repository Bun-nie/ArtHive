from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Artwork, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

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
    return render(request, 'homepage/gallery.html', {'categories': categories, 'artworks': artworks, 'user' : user})

@login_required(login_url='login')
def viewArtwork(request, pk):
    artwork = Artwork.objects.get(id=pk) # for the artwork field view

    # for the comments
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment_body = form.save(commit=False)
            comment_body.user = get_object_or_404(User, id=request.user.id)
            # naa diri ang bug about sa ID
            comment_body.artwork_ref = get_object_or_404(Artwork, id=pk)
            comment_body.save()
        else:
            raise ValidationError("Incorrect data. No ID")
        
    else:
        form = CommentForm()

    return render(request, 'homepage/artwork.html', {
        'artwork': artwork,
        'comment_body' : Comment.objects.filter(artwork_ref__id=pk),
        'form': form
        })
    # until here ang bug

@login_required(login_url='login')
def addArtwork(request):
    user = request.user
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        user = request.user
        artworks = request.FILES.getlist('images', False)

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