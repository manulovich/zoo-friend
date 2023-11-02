from django.shortcuts import render


def pageNotFound(request, exception):
    return render(request, 'page-not-found.pug')