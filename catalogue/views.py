from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse
from django.http import Http404

from catalogue.models import Product


def product_list(request):
    """ 商品一覧画面
    """
    products = Product.objects.order_by('name')
    # 1ページに5商品表示する
    paginator = Paginator(products, 5)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        # ページ番号が数字でない場合、ページ番号が不正な場合は
        # 1ページ目を返す
        products = paginator.page(1)

    return TemplateResponse(request, 'catalogue/product_list.html',
                            {'products': products})


def product_detail(request, product_id):
    """ 商品詳細画面
    """
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404

    return TemplateResponse(request, 'catalogue/product_detail.html',
                            {'product': product})