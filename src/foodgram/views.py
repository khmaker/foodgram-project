import os
from tempfile import NamedTemporaryFile

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import FileResponse
from django.shortcuts import render


def page_not_found(request, exception):
    """404 handler"""
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    """500 handler"""
    return render(request, 'misc/500.html', status=500)


@login_required
def download_cart(request):
    temp = NamedTemporaryFile(delete=False)
    with open(temp.name, 'w+b') as file:
        text = ''
        user = request.user
        cart = user.purchases.prefetch_related('recipe')
        cart = cart.values('recipe__ingredients__title',
                           'recipe__ingredients__unit', )
        ingredients = cart.annotate(amount=Sum('recipe__amount__amount')).all()
        for i in ingredients.order_by('recipe__ingredients__title'):
            title = i.get('recipe__ingredients__title')
            amount = i.get('amount')
            unit = i.get('recipe__ingredients__unit')
            if title is not None:
                text += f'{title}: {amount} {unit}\n'
        file.write(bytes(text, encoding='utf-8'))
        file.seek(0)
    response = FileResponse(open(temp.name, 'rb'),
                            filename='cart.txt',
                            as_attachment=True)
    os.remove(temp.name)
    return response


def about_author(request):
    return render(request, 'misc/about.html')


def about_tech(request):
    return render(request, 'misc/tech.html')
