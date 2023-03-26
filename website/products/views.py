from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

# Create your views here.
def addProduct(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect('Error ')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
