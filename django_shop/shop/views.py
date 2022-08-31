from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, Category
from .forms import FormReview
from .services import review_create, get_product

# Create your views here.


class ProductListView(ListView):
    paginate_by = 15
    context_object_name = "products_list"
    template_name = 'product_list.html'

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs['category_slug']
        )

        if not self.category.is_leaf_node():
            self.context_object_name = "category_list"
            self.template_name = 'category_list.html'
            return self.category.get_children()
        return get_product(self.category.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ProductDetailView(DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormReview
        return context

    def post(self, request, **kwargs):
        form = FormReview(request.POST, request.FILES)
        self.object = super().get_object()
        context = self.get_context_data(**kwargs)

        if not review_create(form, self.object):
            context['form'] = form
        return self.render_to_response(context=context)
