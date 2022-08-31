from .models import Article

def get_articles():
    return Article.objects.order_by('created')
