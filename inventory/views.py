from django.shortcuts import render
from .models import Product, Category, Tag

# Create your views here.
def product_list(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    products = Product.objects.all()                                            # Fetch all products from the database
    products = products.select_related('category').prefetch_related('tags')     # Optimize queries for related fields

    # description search
    search_query = request.GET.get('search', '').strip()                        # Get search query
    if search_query:
        products = products.filter(description__icontains=search_query)         # widecard search in description

    # filter by category
    category_filter = request.GET.get('category', '').strip()                   # Get category filter
    if category_filter:
        products = products.filter(category__name__iexact=category_filter)      # category name match

    # filter by tags
    tag_filters = request.GET.getlist('tag')                                    # Get tag filters
    tag_filters = [tag.strip() for tag in tag_filters if tag.strip()]           # Clean up tag filters
    if tag_filters:
        products = products.filter(tags__name__in=tag_filters)                  # tag name match

    products = products.distinct()                                              # Get distinct results if multiple products match
    
    context = {
        'products': products,
        "categories": categories,
        "tags": tags,
        "search_query": search_query,
        "category_filter": category_filter,
        "tag_filters": tag_filters,
    }

    return render(request, 'inventory.html', context)