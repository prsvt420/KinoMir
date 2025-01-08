from typing import Any, Dict, Optional

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import DetailView, ListView

from core.utils import request_is_ajax
from movies.models import Movie
from movies.services import MovieService


class MoviesListView(ListView):
    """Представление списка фильмов"""

    template_name: str = "movies/movies-list.html"
    model: type[Any | None] = Movie
    context_object_name: str = "movies"

    def get_queryset(self, *args, **kwargs) -> QuerySet[Movie]:
        """
        Метод возвращает список фильмов

        Returns:
            QuerySet[Movie]: Список фильмов
        """

        search_query: Optional[str] = self.request.GET.get("q", "").strip()

        if search_query:
            movies: QuerySet[Movie] = MovieService().get_movies_by_search_query(
                search_query
            )

            if movies.exists():
                return movies

        return MovieService().get_movies()

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse | HttpResponse:
        """
        Метод обрабатывает GET-запрос
        """

        if request_is_ajax(request):
            movies_json = list(self.get_queryset().values())
            return JsonResponse(movies_json, safe=False)

        return super().get(request, *args, **kwargs)


class MovieDetailView(DetailView):
    """Представление конкретного фильма"""

    template_name: str = "movies/movie-detail.html"
    model: type[Any] = Movie
    context_object_name: str = "movie"

    def get_context_data(self, **kwargs) -> Dict:
        """Возвращает словарь с данными для шаблона"""

        context: Dict = super().get_context_data(**kwargs)
        context["film_participants"] = MovieService().get_film_participants(self.object)
        return context
