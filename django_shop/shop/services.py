from .models import Product


def review_create(form, product_review):
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.product = product_review
        new_review.save()
        return True
    return False


def get_product(category_slug):
    return Product.objects.filter(category__slug=category_slug).select_related('category').order_by('id')
