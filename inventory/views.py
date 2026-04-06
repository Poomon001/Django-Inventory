from django.shortcuts import render
from .models import Product, Category, Tag

# Create your views here.
def product_list(request):
    ''' QuerySets for categories, tags, and products lazy evaluations '''
    categories = Category.objects.all()
    tags = Tag.objects.all()
    products = Product.objects.all()

    # description search
    search_query = request.GET.get('search', '').strip()                        # Get search query
    if search_query:
        products = products.filter(description__icontains=search_query)         # insensitive partial match on description

    # filter by category
    category_filter = request.GET.get('category', '').strip()                   # Get category filter
    if category_filter:
        products = products.filter(category__name__iexact=category_filter)      # category name match

    # filter by tags
    tag_filters = request.GET.getlist('tag')                                    # Get tag filters
    tag_filters = [tag.strip() for tag in tag_filters if tag.strip()]           # Clean up tag filters and remove empty values
    if tag_filters:
        products = products.filter(tags__name__in=tag_filters)                  # tag name match

    products = products.select_related('category').prefetch_related('tags')     # Optimize queries to avoid N+1 queries when accessing in the templete
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