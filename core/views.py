from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect


def redirect_to_movies(request: HttpRequest) -> HttpResponseRedirect:
    """Функция перенапраправляет на главную страницу"""
    return redirect('movies:movies-list')
