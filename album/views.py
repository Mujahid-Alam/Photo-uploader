from django.shortcuts import redirect, render

from album.models import Photos

# Create your views here.
def home(request):
    if request.method == "POST":
        p = Photos()
        p.title = request.POST.get('title')
        p.descriptions = request.POST.get('descriptions')
        p.images = request.FILES.get('images')
        p.save()
        return redirect(home)
    # data = {'photos':Photos.objects.all()}
    return render(request, "home.html")   #  <= ,data