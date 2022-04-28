from django.contrib import admin
from .models import (
  ProductPictures, Products, ProductTypes, Manufacturers
)


admin.site.register(
  [ProductTypes, Manufacturers, Products, ProductPictures]
)
