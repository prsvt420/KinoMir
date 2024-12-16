from typing import Optional, Dict, List

from django.db.models import QuerySet
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView

from movies.models import Movie
from movies.services import MovieService
from movies.utils import request_is_ajax


class MoviesListView(ListView):
    """Представление списка фильмов"""

    template_name: str = 'movies/movies-list.html'
    model: Movie = Movie
    context_object_name: str = 'movies'

    def get_queryset(self, *args, **kwargs) -> QuerySet[Movie]:
        """
        Метод возвращает список фильмов

        Returns:
            QuerySet[Movie]: Список фильмов
        """

        search_query: Optional[str] = self.request.GET.get('q')

        if search_query:
            return MovieService().get_movies_by_search_query(search_query)
        return MovieService().get_movies()

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse | HttpResponse:
        """
        Метод обрабатывает GET-запрос
        """

        if request_is_ajax(request):
            movies_json: List[Movie] = list(self.get_queryset().values())
            return JsonResponse(movies_json, safe=False)

        return super().get(request, *args, **kwargs)


class MovieDetailView(DetailView):
    """Представление конкретного фильма"""

    template_name: str = 'movies/movie-detail.html'
    model: Movie = Movie
    context_object_name: str = 'movie'

    def get_context_data(self, **kwargs) -> Dict:
        """Возвращает словарь с данными для шаблона"""

        context = super().get_context_data(**kwargs)
        context['film_participants'] = MovieService().get_film_participants(self.object)
        return context
