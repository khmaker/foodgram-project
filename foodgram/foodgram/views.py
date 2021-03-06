"""Basic views"""

from django.shortcuts import render


def page_not_found(request, exception):
    """404 handler"""
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    """500 handler"""
    return render(request, 'misc/500.html', status=500)
