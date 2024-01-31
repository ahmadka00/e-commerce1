from django.shortcuts import render, get_object_or_404
from store.models import Product, Category


def home(request):
    products = Product.objects.filter(is_active=True)
    recent_viewed_product = []

    if 'recently_viewed' in request.session:
        recently_viewed_ids = request.session['recently_viewed']
        recent_viewed_product = Product.objects.filter(pk__in=recently_viewed_ids)

    recent_viewed_products = sorted(recent_viewed_product, key=lambda x: request.session['recently_viewed'].index(str(x.id)))
    
    request.session.modified = True


    context = {
        'products': products, 
        'recent_viewed_products': recent_viewed_products}
    return render(request, "store/index.html", context ) 

def product_page(request, slug):
    product = get_object_or_404(Product, slug=slug)
    products_related = Product.objects.filter(category=product.category, is_active=True, in_stock=True).exclude(id=product.id)
    product_id = str(product.id)

    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)

        request.session['recently_viewed'].insert(0, product_id)
        if len(request.session['recently_viewed']) > 8:
            request.session['recently_viewed'].pop()

    else: 
        request.session['recently_viewed'] = [product_id]

    
    request.session.modified = True

    context = {'product': product, "products_related":products_related}
    return render(request, 'store/products/single.html', context)


def category_page(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category':category, 'products':products})