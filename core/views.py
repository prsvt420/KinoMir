from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from core.forms import FeedbackForm
from core.tasks import send_feedback


class FeedbackView(FormView):
    """Представление обратной связи"""

    template_name: str = 'core/feedback.html'
    form_class: type = FeedbackForm
    success_url: str = reverse_lazy('movies:movies-list')

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Метод обработки POST-запроса"""

        send_feedback.delay(data=request.POST)

        return super().post(request, *args, **kwargs)


def redirect_to_movies_list(request: HttpRequest) -> HttpResponseRedirect:
    """Редирект на список фильмов"""
    return redirect('movies:movies-list')
