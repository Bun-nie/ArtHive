from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Artwork, Comments
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from homepage.forms import CommentForm
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
# Prgrmr: Alimurung

@login_required(login_url='base: login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    
    if category == None:
        artworks = Artwork.objects.all()
    else:
        artworks = Artwork.objects.filter(category__name = category, category__user = user)

    categories = Category.objects.all()
    # context = {'categories': categories, 'artworks': artworks}
    return render(request, 'homepage/gallery.html', {'categories': categories, 'artworks': artworks})

@login_required(login_url='base: login')
def viewArtwork(request, pk):
    artwork_post = Artwork.objects.get(id=pk)
    form = CommentForm()
    context = {
        'artwork_post' : artwork_post,
        'form' : form,
    }
    # comment_section = Comments.objects.get(id=pk)

    return render(request, 'homepage/artwork.html', context)

@login_required(login_url='base: login')
def addArtwork(request):
    user = request.user
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
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

        # aw stands for artwork. i can't make another variable using 'artwork' as it is being used inside the for loop  
        for aw in artworks:
            artwork = Artwork.objects.create(
                category = category,
                description = data['description'],
                artwork = aw,
            )
        return redirect('base:gallery')

    context = {'categories': categories}
    return render(request, 'homepage/add.html', context)

@login_required
def artworkPostEditView(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    if request.method == "POST":

        body = request.POST.get('body', '')
        if body:
            artwork.description = body
            artwork.save()
            return redirect(reverse_lazy('viewArtwork', kwargs = {'pk':pk}))    
        
    return render(request, 'homepage/edit_post.html', {'artwork':artwork})
    
    
    
    # model = Artwork 
    # fields = ['body']
    # template_name = 'homepage/edit_post.html'

    # def get_success_url(self):
    #    pk = self.kwargs['pk']
    #    return reverse_lazy('viewArtwork', kwargs = {'pk':pk})

# first draft
# @login_required
# def addComment(request, pk, artwork):
#     user = request.user
#     comments = Comments.objects.get(id=pk)
    
#     context = {'comments': comments}
#     return render(request, 'homepage/artwork.html', context)