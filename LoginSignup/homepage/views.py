from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Artwork, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, ArtworkForm
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
    # artwork = Artwork.objects.get(id=pk) # for the artwork field view
    artwork = get_object_or_404(Artwork, id=pk)

    # for the comments
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            # naa diri ang bug about sa ID
            comment.artwork_ref = artwork
            comment.save()
            form = CommentForm()
        else:
            # raise ValidationError("Incorrect data. No ID")
            form.add_error(None, "Incorrect data provided.")

    else:
        form = CommentForm()

    comments = Comment.objects.filter(artwork_ref=artwork)

    return render(request, 'homepage/artwork.html', {
        'artwork': artwork,
        'comments': comments,
        'form': form,
        'artwork_pk': artwork.id
        })

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

# View for editing comment
@login_required(login_url='login')
def editComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user == comment.user:
        if request.method == 'POST':
            comment_body = request.POST.get('comment_body', '')
            comment_image = request.FILES.get('comment_image')

            comment.comment_body = comment_body
            if comment_image:
                comment.comment_image = comment_image
            comment.save()

            return JsonResponse({'status': 'success', 'comment_body': comment.comment_body, 'comment_image_url': comment.comment_image.url if comment.comment_image else None})

    return JsonResponse({'status': 'error', 'message': 'Unauthorized action'}, status=403)

# View for deleting comment
@login_required(login_url='login')
def deleteComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user == comment.user:
        comment.delete()
        return JsonResponse({'status': 'success', 'message': 'Comment deleted successfully'})

    return JsonResponse({'status': 'error', 'message': 'Unauthorized action'}, status=403)

def edit_artwork(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)

    # Check if the logged-in user is the owner
    if request.user != artwork.user:
        return redirect('base:gallery')  # or any other page, maybe a 403 forbidden

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('base:view_artwork', pk=artwork.pk)
    else:
        form = ArtworkForm(instance=artwork)

    return render(request, 'homepage/edit_artwork.html', {'form': form, 'artwork': artwork})