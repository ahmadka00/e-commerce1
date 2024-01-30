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

# def product_page(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     # retrive products related 
#     products_related = Product.objects.filter(category=product.category, is_active=True, in_stock=True).exclude(id=product.id)
#     user = request.user

#     # create session for recent view product 

#     product_id = request.GET.get('product_id')

#     if product_id:
#         # Your existing logic for recently viewed products
#         recent_viewed_session = request.session.get('recent_viewed', [])
        
#         if product_id in recent_viewed_session:
#             recent_viewed_session.remove(product_id)

#         recent_viewed_session.insert(0, product_id)

#         if len(recent_viewed_session) > 8:
#             recent_viewed_session.pop()

#         recent_viewed_products = Product.objects.filter(pk__in=recent_viewed_session)
#         recent_viewed_products = sorted(recent_viewed_products, key=lambda x: recent_viewed_session.index(x.id))

#         request.session['recent_viewed'] = recent_viewed_session
#         request.session.modified = True

#     else:
#         # Handle the case when product_id is not present in the query string
#         recent_viewed_products = []



    
#     request.session.modified = True

#     context = {
#         'product':product, 
#         'products':products_related,
#         'user':user,
#         'recent_viewed_products':recent_viewed_products
#     }

#     return render(request, 'store/products/single.html', context)

def category_page(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category':category, 'products':products})