def cart_counter(request):
    user = request.user
    count = user.purchases.all().count() if user.is_authenticated else 0
    return {'cart_counter': count, }
