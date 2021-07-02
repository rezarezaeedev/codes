from django.db import models

class ProductQuerySet(models.query.QuerySet):
    def get_featured(self):
        return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    # overriding get_queryset
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    # My custom filters
    def all(self):
        return self.get_queryset().active()

    def get_featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self, productId):
        qs = self.get_queryset().filter(id=productId)  # Product.objects
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=10.36)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    # overriding objects field in class -same of: Product.objects
    objects = ProductManager()


"""
Using: in views

context={
   'products': products = Product.objects.all().featured().active()
}

"""





















