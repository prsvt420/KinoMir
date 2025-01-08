from typing import Optional, Dict, Any

from django.db.models import QuerySet
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView

from core.utils import request_is_ajax
from serials.models import Serial
from serials.services import SerialService


class SerialsListView(ListView):
    """Представление списка сериалов"""

    template_name: str = 'serials/serials-list.html'
    model: type[Any | None] = Serial
    context_object_name: str = 'serials'

    def get_queryset(self, *args, **kwargs) -> QuerySet[Serial]:
        """
        Метод возвращает список сериалов

        Returns:
            QuerySet[Serial]: Список сериалов
        """

        search_query: Optional[str] = self.request.GET.get('q', '').strip()

        if search_query:
            serials: QuerySet[Serial] = SerialService().get_serials_by_search_query(search_query)

            if serials.exists():
                return serials

        return SerialService().get_serials()

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse | HttpResponse:
        """
        Метод обрабатывает GET-запрос
        """

        if request_is_ajax(request):
            serials_json = list(self.get_queryset().values())
            return JsonResponse(serials_json, safe=False)

        return super().get(request, *args, **kwargs)


class SerialDetailView(DetailView):
    """Представление конкретного сериала"""

    template_name: str = 'serials/serial-detail.html'
    model: type[Any] = Serial
    context_object_name: str = 'serial'

    def get_context_data(self, **kwargs) -> Dict:
        """Возвращает словарь с данными для шаблона"""

        context: Dict = super().get_context_data(**kwargs)
        context['serial_participants'] = SerialService().get_serial_participants(self.object)
        return context
