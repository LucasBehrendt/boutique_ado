from django.shortcuts import render


def view_bag(request):
    """Renders bag page"""
    return render(request, 'bag/bag.html')
