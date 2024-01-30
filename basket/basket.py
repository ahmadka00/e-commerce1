from store.models import Product
from decimal import Decimal

class Basket():


    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket_key')
        if 'basket_key' not in request.session:
            basket = self.session['basket_key'] = {}
        self.basket = basket

    def add(self, product, qty):

        product_id = str(product.id)
        if product_id in self.basket:
            pass
        else:
            self.basket[product_id] = {'price':str(product.price), 'qty':int(qty)}
        
        self.save()
        

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    def __len__(self):
        """
        Get the basket data and count the qty of item
        """
        return sum(item['qty'] for item in self.basket.values())
        

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
    

    def delete(self, product):

        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            
        self.save()



    def save(self):
        self.session.modified = True
