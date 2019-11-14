from django.contrib import admin
from .models import Product, ImageProduct, ProductCategory
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ImageProduct
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]


    class Meta:
        model = Product

class ImageProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ImageProduct._meta.fields]


    class Meta:
        model = ImageProduct
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]


    class Meta:
        model = ProductCategory


admin.site.register(ImageProduct, ImageProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)


